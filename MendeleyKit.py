import urllib.parse
import requests
import webbrowser

client_id = '16108'
client_secret = 'wuOnluFIZ62PyKDH'
redirect_uri = 'https://locallhost.com/'
authorize_url = 'https://api-oauth2.mendeley.com/oauth/authorize'
token_url = 'https://api-oauth2.mendeley.com/oauth/token'
state = 'Jeans_for_All'


def get_authorization_url():
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "all",
        "state": state
    }

    url = authorize_url + "?" + urllib.parse.urlencode(params)
    return url


def exchange_authorization_code(code):
    post_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    feedback = requests.post(token_url, data=post_data)
    token_json = feedback.json()

    if "error" in token_json:
        error_message = token_json.get("error_description", "Unknown error occurred")
        raise Exception(f"Token Exchange Error: {error_message}")

    return token_json["access_token"], token_json['refresh_token']


if __name__ == '__main__':
    authorization_url = get_authorization_url()
    print("Opening authorization URL in your default web browser...")
    print(f'Authorization URL: {authorization_url}')
    webbrowser.open(authorization_url)
    print("Please complete the authorization process in your web browser.")
    authorization_code = input("Enter the authorization code: ")

    try:
        access_token, refresh_token = exchange_authorization_code(authorization_code)
        print("Access Token:", access_token)
        print("Refresh Token:", refresh_token)

        import json
        data = {'Access token': access_token, 'Refresh token': refresh_token}
        with open('tokens.json', 'w') as f:
            json.dump(data, f)

    except Exception as e:
        print("Token exchange failed:", str(e))

# import requests
#
# # Mendeley API configuration
# client_id = '16105'
# client_secret = 'scrlvIxxDYMt5Uqg'
# redirect_uri = 'https://localhost.com/'  # Fixed typo in the redirect_uri
# authorize_url = 'https://api-oauth2.mendeley.com/oauth/authorize'
# token_url = 'https://api-oauth2.mendeley.com/oauth/token'
#
# # Token information (please handle tokens securely in practice)
# access_token = 'MSwxNjkyMzU0Nzk1NzMzLDcyMTYzNTUxMSwxNjEwNSxhbGwsLCw5YjZmYTQyNjI1OWI1NzQ2ZDA0OGRkZjY5MzFkODY0MTEwY2FneHJxYSw3N2Y0M2ZlOS01ZWM3LTM5NDQtODJjOS1mMThjNTZlMGU3ZTMsamNGNEVsTlVaakR1S1V5M3ptdl9vdUNSN3lF'
# refresh_token = 'MSw3MjE2MzU1MTEsMTYxMDUsYWxsLCwsLDc3ZjQzZmU5LTVlYzctMzk0NC04MmM5LWYxOGM1NmUwZTdlMyxub3QtdXNlZCxub3QtdXNlZCw5YjZmYTQyNjI1OWI1NzQ2ZDA0OGRkZjY5MzFkODY0MTEwY2FneHJxYSwxNjkyMjU2MTk5MTkxLFBCaURGNjMwSEZtTktkWU12WlR5WFppRndOcw'
#
#
# def refresh_access_token(refresh_token):
#     post_data = {
#         "grant_type": "refresh_token",
#         "refresh_token": refresh_token,
#         "client_id": client_id,
#         "client_secret": client_secret
#     }
#
#     response = requests.post(token_url, data=post_data)
#     token_json = response.json()
#
#     if "error" in token_json:
#         error_message = token_json.get("error_description", "Unknown error occurred")
#         raise Exception(f"Token Refresh Error: {error_message}")
#
#     return token_json["access_token"], token_json['refresh_token']
#
#
# def search_documents_by_query(query, access_token):
#     base_url = 'https://api.mendeley.com'
#     endpoint = '/catalogV1'
#     headers = {
#         "Authorization": f"Bearer {access_token}",
#         "Accept": "application/vnd.mendeley-document.1+json"
#     }
#     params = {
#         "query": query
#     }
#
#     try:
#         response = requests.get(base_url + endpoint, headers=headers, params=params)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print('Request error:', e)
#         return None
#
#
# if __name__ == '__main__':
#     search_query = 'Bioenergy crops as alternative feedstocks for recovery of anthocyanins: A review'
#
#     # Handle token refreshing here if needed
#     # access_token, refresh_token = refresh_access_token(refresh_token)
#
#     documents = search_documents_by_query(search_query, access_token)
#
#     if documents:
#         print("Search Results:")
#         for doc in documents:
#             print("Title:", doc.get("title", "N/A"))
#             author_names = [f"{author['first_name']} {author['last_name']}" for author in doc.get("authors", [])]
#             print("Authors:", ", ".join(author_names))
#             print("Year:", doc.get("year", "N/A"))
#             print("Abstract:", doc.get("abstract", "N/A"))
#             print("=" * 50)
#     else:
#         print("Search request failed.")
