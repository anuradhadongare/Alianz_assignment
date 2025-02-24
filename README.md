# Hockey Stats Scraper

This project scrapes hockey team statistics from [https://www.scrapethissite.com/pages/forms/](https://www.scrapethissite.com/pages/forms/) and generates an Excel file with the data and a summary of winners and losers per year.  It also saves the raw HTML files in a zip archive.

## Requirements

- Python 3.13.2
- The required Python libraries are listed in `requirements.txt`.

## Installation

1. Clone the repository (or download the zip and extract it).
2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv .venv  # On Windows: python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. To run the scraper  Bash  python hockey_scraper.py
   This will:
   Scrape the data from the website.
   Create hockey_stats.xlsx containing the scraped data and summary.
   Create html_files.zip containing the raw HTML files
4. Running Tests
   To run the unit tests: pytest --html=report.html 
5. output :
   hockey_stats.xlsx: Excel file with the scraped data and summary.
   html_files.zip: Zip archive containing the raw HTML files.
6. you can use excel viewer to view the excel file and the result of testing is generate in report.html that can be viewed
   in the browser.
7. install the below lib files:
   pip install aiohttp
   pip install bs4
   pip install openpyxl
   pip install pytest
   pip install pytest-html
  



