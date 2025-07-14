'''4. Жестко закодированные учетные данные
Примеры: Наличие в коде репозиториев паролей, ключей API, токенов и других чувствительных данных.'''

import re
from api import get_content

patterns = [
    r'API[_-]KEY\s*=\s*[\'"][a-zA-Z0-9_-]+[\'"]',
    r'password\s*=\s*[\'"][a-zA-Z0-9_-]+[\'"]',
    r'secret\s*=\s*[\'"][a-zA-Z0-9_-]+[\'"]',
    r'token\s*=\s*[\'"][a-zA-Z0-9_-]+[\'"]',
]

def search_sensitive_data(response):
    result = []
    for item in response:
        file_url = item['html_url']
        raw_url = item['url']
        raw_response = get_content(raw_url)
        for pattern in patterns:
            matches = re.findall(pattern, raw_response)
            if matches:
                keywords = []
                for match in matches:
                    keywords.push(match)
                result.push({
                    'repository': 'https://github.com/' + item['repository']['full_name'],
                    'keywords': keywords,
                    'module': file_url,
                    'type': 'sensitive data',
                })
    return result
