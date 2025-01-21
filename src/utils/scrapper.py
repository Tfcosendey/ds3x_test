import requests
from bs4 import BeautifulSoup

def scrapper(url, file_path):
    """
    Scrapes a webpage to find a download link and saves the file locally.

    Args:
        url (str): The URL of the webpage to scrape.
        file_path (str): The local file path where the downloaded file will be saved.

    Raises:
        requests.exceptions.RequestException: If there is a network-related error or an invalid response.
        Exception: For any other errors that occur during the scraping or file download process.

    Returns:
        str: The file path of the saved file.
    """
    try:
        # Send a GET request to fetch the webpage
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the download link (based on the class found in the dev tools)
        download_link = soup.find('a', class_='download')['href']

        # Download the file
        file_response = requests.get(download_link)

        # Save the file locally
        with open(file_path, 'wb') as file:
            file.write(file_response.content)

        print(f"File saved to: {file_path}")

        return file_path

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the network request: {e}")
        raise e
    except Exception as e:
        print(f"An error occurred during scraping or file download: {e}")
        raise e
