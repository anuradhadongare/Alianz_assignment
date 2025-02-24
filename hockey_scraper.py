import asyncio
import aiohttp
from bs4 import BeautifulSoup
import zipfile
import openpyxl
from collections import defaultdict

async def fetch_page(session, url, page_num):
    async with session.get(url) as response:
        if response.status == 200:
            html = await response.text()
            with zipfile.ZipFile("html_files.zip", "a") as zf:
                zf.writestr(f"{page_num}.html", html)  # Store in zip
            return html
        else:
            print(f"Error fetching {url}: {response.status}")
            return None

async def scrape_data(session, base_url, num_pages):
    all_data = []
    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        html = await fetch_page(session, url, page)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find("table", class_="table")
            if table:
                rows = table.find_all("tr")[1:] # Skip header
                for row in rows:
                    cells = row.find_all("td")
                    row_data = [cell.text.strip() for cell in cells]
                    all_data.append(row_data)
        await asyncio.sleep(0.1) # Be polite

    return all_data

def analyze_data(data):
    yearly_stats = defaultdict(lambda: {"wins": defaultdict(int), "losses": defaultdict(int)})
    for row in data:
        year = int(row[1].split('-')[0]) # Extract Year
        team = row[0]
        wins = int(row[2])
        yearly_stats[year]["wins"][team] += wins

    summary = []
    for year, stats in yearly_stats.items():
      wins_data = stats["wins"]
      if wins_data: # Check if data exists for the year
        winner = max(wins_data, key=wins_data.get)
        winner_wins = wins_data[winner]
        loser = min(wins_data, key=wins_data.get)
        loser_wins = wins_data[loser]
        summary.append([year, winner, winner_wins, loser, loser_wins])

    return summary

async def main():
    base_url = "https://www.scrapethissite.com/pages/forms/"
    num_pages = 24  # Determined by inspecting the site
    async with aiohttp.ClientSession() as session:
        all_data = await scrape_data(session, base_url, num_pages)

    if all_data:
        workbook = openpyxl.Workbook()
        sheet1 = workbook.active
        sheet1.title = "NHL Stats 1990-2011"
        sheet1.append(["Team", "Season", "Wins", "Losses"]) # Header
        for row in all_data:
            sheet1.append(row)

        summary_data = analyze_data(all_data)
        sheet2 = workbook.create_sheet("Winner and Loser per Year")
        sheet2.append(["Year", "Winner", "Winner Num. of Wins", "Loser", "Loser Num. of Wins"])
        for row in summary_data:
            sheet2.append(row)

        workbook.save("hockey_stats.xlsx")
        print("Data scraped and saved to hockey_stats.xlsx and html_files.zip")

if __name__ == "__main__":
    asyncio.run(main())
