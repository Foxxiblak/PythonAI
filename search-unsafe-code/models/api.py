import requests
import base64
from config import GITHUB_TOKEN, GITHUB_API_URL, SEARCH_CODE
from static.scripts.classifier import vulnerabilities
from views.data_processing import parse_github_response

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

languages_and_keywords = {
    'python': ['django', 'flask'],
    'java': ['spring', 'hibernate', 'struts'],
    'c#': ['wpf'],
}

def params(index_val):
    queries = []
    for language, keywords in languages_and_keywords.items():
        query = f'{vulnerabilities[index_val].keyword} in:file language:{language}'
        queries.append(query)
    return queries, language

def get_response(index_val):
    queries, language = params(index_val)
    res = []
    for query in queries:
        response = requests.get(f"{GITHUB_API_URL}{SEARCH_CODE}", headers=headers, params={'q': query})
        if response.status_code == 200:
            res = parse_github_response(response.json()['items'], language, index_val)
        else:
            print(f"Error in search data: {response.status_code}")
    return res

def get_content(raw_url):
    response = requests.get(raw_url, headers=headers)
    if response.status_code == 200:
        content_data = response.json()
        base64_content = content_data['content']
        decoded_bytes = base64.b64decode(base64_content)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    else:
        print(f"Error in parse html data: {response.status_code}")
        return ''
