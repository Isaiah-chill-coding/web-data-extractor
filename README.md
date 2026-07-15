# Web Data Extractor

A Python automation tool that extracts structured information from public websites and exports the results into CSV or Excel files.

## Overview

Many businesses rely on information published on websites but spend significant time manually copying data into spreadsheets for analysis or reporting. This project automates that process by extracting structured information from webpages and exporting it into organized spreadsheet formats.

The current version demonstrates web scraping using the Books to Scrape practice website. The overall architecture is designed to be adapted to other websites by modifying the HTML selectors.

This project was built as part of a growing portfolio of Python automation tools focused on data extraction and business workflow automation.

## Features

### Current Features

- Download webpage content using Requests
- Parse HTML using BeautifulSoup
- Extract structured product information
- Export results to CSV
- Export results to Excel (.xlsx)
- Input validation for export format

### Extracted Fields

- Product Title
- Price
- Availability
- Rating
- Product URL

## Planned Features

- Selenium support for JavaScript-heavy websites
- Configurable CSS selectors
- Multi-page scraping
- Automatic pagination
- Better error handling
- Logging
- Export to additional file formats

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Pandas
- OpenPyXL

## Project Structure

```text
web-data-extractor/
├── extractor.py
├── output/
│   ├── scraped_data.csv
│   └── scraped_data.xlsx
├── README.md
└── requirements.txt
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run:

```bash
python extractor.py
```

2. Enter the URL of the webpage you want to scrape.

3. Select the export format:

- Excel (.xlsx)
- CSV

4. The extracted data will be exported to the project directory.

## Example Output

| Title | Price | Availability | Rating |
|-------|------:|--------------|--------|
| A Light in the Attic | £51.77 | In Stock | Three |
| Tipping the Velvet | £53.74 | In Stock | One |

## Example Use Cases

- Product catalog collection
- Price monitoring
- Business research
- Public directory extraction
- Data collection for analysis
- Spreadsheet automation

## Future Improvements

- Dynamic website support with Selenium
- Login automation
- Infinite scrolling support
- Configurable scraping templates
- GUI interface
- Batch website processing