import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = []

    # Example: Scraping article titles and links from a blog page
    articles = soup.find_all('article')
    for article in articles:
        title_tag = article.find('h2')
        link_tag = article.find('a')

        # Check if the title and link tags are found
        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag['href']
            data.append({'Title': title, 'Link': link})
        else:
            print(f"Skipping an article due to missing title or link: {article}")

    return data


def save_to_csv(data, filename):
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")


def main():
    url = 'https://pinchofyum.com/'  # Replace with the target URL
    html = fetch_page(url)
    if html:
        data = parse_page(html)
        if data:
            save_to_csv(data, 'scraped_data.csv')
        else:
            print("No data was parsed.")
    else:
        print("Failed to fetch the web page.")


if __name__ == '__main__':
    main()
