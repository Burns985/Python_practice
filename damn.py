import requests

# URL of the webpage
url = "https://testautomationpractice.blogspot.com/"

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    print(html_content)  # This will print the entire HTML of the webpage
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
