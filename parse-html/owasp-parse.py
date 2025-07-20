import requests
from bs4 import BeautifulSoup

owasp_url = 'https://owasp.org/www-project-top-ten/'
def get_title(soup):
    return soup.title.string
def get_top_title(soup):
    return soup.find("h2", id="top-10-web-application-security-risks").string

def get_top10(soup):
    section = soup.find('section', class_='page-body')
    items = section.find_all("li")
    top = []

    for li in items:
        a = li.find("a")
        strong = a.find("strong") if a else None
        if strong:
            title = strong.get_text(strip=True)
            link = a["href"]
            desc = li.get_text(strip=True).replace(title, "").strip()
            top.append({"title": title, "link": link, "description": desc})

    return top

if __name__ == '__main__':
    response = requests.get(owasp_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f'Title: {get_title(soup)}')
    print(get_top_title(soup), end='\n\n')
    top10 = get_top10(soup)
    for item in top10:
        print(f'Vulnerability: {item["title"]} \nLink: {item["link"]} \nDescription: {item["description"]}', end='\n' + '-'*120 + '\n')

