import requests
from bs4 import BeautifulSoup

base_url = 'https://owasp.org/'
owasp_top = f'{base_url}/www-project-top-ten/'
response_top = requests.get(owasp_top)
soup_top = BeautifulSoup(response_top.text, 'html.parser')

owasp_about = f'{base_url}/about/'
response_about = requests.get(owasp_about)
soup_about = BeautifulSoup(response_about.text, 'html.parser')

owasp_contact = f'{base_url}/contact/'
response_contact = requests.get(owasp_contact)
soup_contact = BeautifulSoup(response_contact.text, 'html.parser')
def get_title():
    return soup_top.title.string
def get_top_title():
    return soup_top.find("h2", id="top-10-web-application-security-risks").string

def get_top10():
    section = soup_top.find('section', class_='page-body')
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

def about():
    body = soup_about.find('div', id='main')
    items_p = body.find_all("p")[1:3]
    items_ul = body.find_all("ul")[0]
    items_li = items_ul.find_all("li")
    answer = f'{items_p[0].string}\n'
    for item in items_li:
        answer += f'- {item.string}\n'
    answer += f'{items_p[1].string}'
    return answer

def get_donate_link():
    link_tag = soup_about.find("a", string="Donate")
    if link_tag:
        href = link_tag.get("href")
        donate_link = f"{base_url}{href}" if href.startswith("/") else href
    return donate_link

def get_contact():
    contact = soup_contact.find_all("code")
    global_address = soup_contact.find_all('p')[4].string
    eu_address = soup_about.find_all('p')[6].string
    address = [{'point': global_address, 'address': f'{contact[0].string}\n{contact[1].string}'},
               {'point': eu_address, 'address': f'{contact[2].string}\n{contact[3].string}'}]
    return address

if __name__ == '__main__':
    print(f'Title: {get_title()}')
    print(get_top_title(), end='\n\n')
    top10 = get_top10()
    for item in top10:
        print(f'Vulnerability: {item["title"]} \nLink: {item["link"]} \nDescription: {item["description"]}', end='\n' + '-'*120 + '\n')
    print(f'About: {about()}')
    address = get_contact()
    for item in address:
        print(f'{item["point"]}\n{item["address"]}')

