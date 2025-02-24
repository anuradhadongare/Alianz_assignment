# Hockey Stats Scraper

This project scrapes hockey team statistics from [https://www.scrapethissite.com/pages/forms/](https://www.scrapethissite.com/pages/forms/) and generates an Excel file with the data and a summary of winners and losers per year.  It also saves the raw HTML files in a zip archive.

## Requirements

- Python 3.7+
- The required Python libraries are listed in `requirements.txt`.

## Installation

1. Clone the repository (or download the zip and extract it).
2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv .venv  # On Windows: python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
