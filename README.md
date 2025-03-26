# Job Scraping Project

## Description

This project is designed to scrape job listings from a mock job board website provided by Real Python. The script extracts relevant information about each job, including:

- **Job Title**
- **Company Name**
- **Location (City)**
- **Location (State)**
- **Date Posted**

The date posted is parsed and converted into two additional columns:

- **Day, Month, Day of Week** (e.g., "Thursday, 8 April")
- **Year** (e.g., "2021")

The data is then saved in a **CSV** file, `job_listings.csv`, which can be further analyzed or processed.

This project showcases how web scraping can be applied to extract and organize data from static websites.

## Requirements

To run the script, you need Python installed on your machine along with the required dependencies:

- **requests** - to send HTTP requests and fetch the website content.
- **BeautifulSoup (from `bs4`)** - for parsing HTML content and extracting data.
- **pandas** - to store and manipulate the extracted data and save it to a CSV file.
