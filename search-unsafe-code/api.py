import requests
import base64
from config import GITHUB_TOKEN, GITHUB_API_URL

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

languages_and_keywords = {
    'python': ['django', 'flask'],
    'java': [],
    'c#': [],
}

def params():
    queries = []
    for language, keywords in languages_and_keywords.items():
        if keywords:
            for keyword in keywords:
                query = f'{keyword}+language:{language}'
                queries.append(query)
        else:
            queries.append(f'language:{language}')
    return queries

def get_response():
    queries = params()
    res = []
    for query in queries:
        response = requests.get(GITHUB_API_URL, headers=headers, params={'q': query})
        if response.status_code == 200:
            res += response.json()['items']
        else:
            print(f"Error in search data: {response.status_code}")
            return []
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