import requests
from bs4 import BeautifulSoup
import json
from datetime import date, timedelta

# Base URL of the page containing the data
base_url = 'https://indiankanoon.org/search/?formInput=doctypes%3A%20supremecourt%20fromdate%3A%20{from_date}%20todate%3A%20{to_date}&pagenum='

# Initialize a list to store all the data
data_list = []

# Initialize the start date and end date
start_date = date(1947, 1, 1)
end_date = date(2023, 9, 1)

# Loop through each month from start date to end date
while start_date < end_date:
    # Get the first and last day of the current month
    from_date = start_date.replace(day=1)
    to_date = (from_date + timedelta(days=31)).replace(day=1) - timedelta(days=1)

    # Convert the dates to strings in the format dd-mm-yyyy
    from_date_str = from_date.strftime('%d-%m-%Y')
    to_date_str = to_date.strftime('%d-%m-%Y')

    # Construct the URL for the current month
    url = f'{base_url.format(from_date=from_date_str, to_date=to_date_str)}'

    # Initialize the page number for the current month
    page = 1

    while True:
        # Append the page number to the URL
        url_with_page = f'{url}{page}'

        # Send an HTTP GET request to the URL
        response = requests.get(url_with_page)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the <div> elements with class "result"
            result_divs = soup.find_all('div', class_='result')

            # If no results are found, break the loop
            if not result_divs:
                break

            # Loop through the result divs and extract the document name and link
            for result_div in result_divs:
                document_name = result_div.find('a').text.strip()
                document_link = result_div.find('a')['href']

                # Create a dictionary for each document
                document_data = {
                    'document_name': document_name,
                    'document_link': document_link
                }

                # Append the dictionary to the data list
                data_list.append(document_data)

            # Increment the page number for the next iteration
            page += 1

        else:
            print(f'Failed to retrieve page {page} for month {from_date_str} - {to_date_str}.')
            break

    # Increment the start date by one month for the next iteration
    start_date = to_date + timedelta(days=1)

# Save the data to a JSON file
with open('scraped_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print('Data has been scraped from all pages and saved to "scraped_data.json".')
