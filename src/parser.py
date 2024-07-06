from bs4 import BeautifulSoup


def parse_articles(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    articles = soup.find_all('div', class_='top-newslist')
    data = []
    for article in articles:
        title = article.find('a').get_text(strip=True)
        link = article.find('a').get('href')
        if link.startswith('/'):
            link = 'https://timesofindia.indiatimes.com' + link
        data.append({'title': title, 'link': link})
    return data
