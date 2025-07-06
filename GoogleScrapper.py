import requests
from bs4 import BeautifulSoup
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#
# </body>
# </html>

class GoogleWebResultsScraper:
    def __init__(self):
        self.base_url = "https://www.google.com/search"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.3"
        }

    def scrape(self, query, num_results=10):
        params = {
            "q": query,
            "num": num_results
        }
        try:
            response = requests.get(self.base_url, params=params, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"An error occurred while making the request: {e}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for result in soup.select("div.g"):
            link = result.select_one("a[href]").get("href")
            title = result.select_one("h3").text
            description = result.select_one("div.IsZvec").text
            results.append({
                "title": title,
                "link": link,
                "description": description
            })
        return results


# Example usage:
if __name__ == "__main__":
    query = "Python programming"
    num_results = 5
    scraper = GoogleWebResultsScraper()
    results = scraper.scrape(query, num_results)
    for i, result in enumerate(results, start=1):
        print(f"Result {i}:")
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Description: {result['description']}")
        print()
