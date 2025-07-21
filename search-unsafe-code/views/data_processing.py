import json
from static.scripts.classifier import vulnerabilities

def parse_github_response(items: [], lng: str, index_val):
    data = []
    for item in items:
        print(item, end="\n\n\n\n\n\n\n")
        data.append({
            item['html_url']: {
                'language': lng,
                'class': vulnerabilities[index_val].class_id,
                'name': vulnerabilities[index_val].name,
                'level': vulnerabilities[index_val].level.value,
                'owner': {
                    "login":  item['repository']['owner']['login'],
                    "avatar_url": item['repository']['owner']['avatar_url'],
                    "repo": item['repository']['owner']['html_url']
                },
            }
        })
    return data
    #save_file(data, vulnerabilities[index_val].class_id)

def save_file(data, file_name):
    with open(f"{file_name}.json", "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Сохранено {len(data)} результатов в {file_name}")