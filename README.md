# Supreme Court Case Scraper

This Python script scrapes case names and links from the Indian Kanoon website (https://indiankanoon.org/) for all Supreme Court cases from January 1, 1947, to September 1, 2023. The scraped data is saved in a JSON file named `scraped_data.json`.

2. Save the provided code in a Python file (e.g., `scraper.py`).

## Usage

1. Run the script
2. The script will start scraping the website and saving the data to the `scraped_data.json` file.
3. Once the scraping is complete, a message will be printed indicating that the data has been saved to the JSON file.

## How it Works

1. The script constructs a base URL for the Indian Kanoon search page, with placeholders for the start and end dates.
2. It loops through each month from January 1, 1947, to September 1, 2023.
3. For each month, it constructs the search URL with the appropriate start and end dates.
4. The script then sends an HTTP GET request to the search URL and parses the HTML content using BeautifulSoup.
5. It extracts the document names and links from the search results and stores them in a list of dictionaries.
6. If there are no more search results for the current month, the loop moves to the next month.
7. After scraping all the data, the script saves the list of dictionaries to a JSON file named `scraped_data.json`.
