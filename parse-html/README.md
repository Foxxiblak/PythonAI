## HTML Parser for OWASP & Web Content
This project is designed for parsing HTML pages using BeautifulSoup. The main task is to extract structured information from the OWASP website, including threat lists, descriptions, and other elements.

## Tech stack:
    •    Python 3.11+
    •    BeautifulSoup4
    •    requests
    •    [telegram bot]

## Installation:
pip install beautifulsoup4 requests

## Run:
python owasp_parse.py

## Features:
•    Retrieve OWASP Top 10 from owasp.org
•    Extract  list from the desired block
•    Get links by text (e.g., Donate, Contacts etc.)
•    Process HTML from a local file or via requests

## Telegram bot commands @OWASP_info_bot:
/about - What is OWASP
/top - Get top 10 vulnerabilities
/donate - Donate to the team
/contact - Get team contacts
