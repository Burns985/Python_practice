import requests

client_id = '16105'
client_secret = 'scrlvIxxDYMt5Uqg'
redirect_uri = 'https://locallhost.com/'
authorize_url = 'https://api-oauth2.mendeley.com/oauth/authorize'
token_url = 'https://api-oauth2.mendeley.com/oauth/token'
state = 'Jeans_for_All'


def refresh_access_token(refresh_token):
    post_data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    feedback = requests.post(token_url, data=post_data)
    token_json = feedback.json()

    if "error" in token_json:
        error_message = token_json.get("error_description", "Unknown error occurred")
        raise Exception(f"Token Refresh Error: {error_message}")

    return token_json["access_token"], token_json['refresh_token']


def search_documents_by_catalog(query, access_token):
    base_url = 'https://api.mendeley.com'
    endpoint = '/catalog'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.mendeley-document.1+json"
    }
    params = {
        "limit": "20",
        "query": query
    }

    try:
        response = requests.get(base_url + endpoint, headers=headers, params=params)
        print(response.text)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print('Request error:', e)
        return None


def get_document_info_by_id(doc_id, access_token):
    base_url = 'https://api.mendeley.com'
    endpoint = f'/id/{doc_id}/'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.mendeley-document.1+json"
    }
    # params = {
    #     "id": doc_id
    # }

    try:
        #                                                           , params = params
        response = requests.get(base_url + endpoint, headers=headers)
        print(response.text)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print('Request error:', e)
        return None


if __name__ == '__main__':
    import json

    search_query = 'Data Science'

    with open('tokens.json', 'r') as f:
        data = json.load(f)

    tokens = {'Access Token': data['Access token'], 'Refresh token': data['Refresh token']}

    documents = search_documents_by_catalog(search_query, tokens['Access Token'])

    if documents:
        print("Documents:")
        for doc in documents['documents']:
            print(f'id = {doc["id"]}')
            print(f'url = {doc["url"]}')
            print(get_document_info_by_id(doc["id"], tokens['Access Token']))
            break
    else:
        print("Search request failed.")
