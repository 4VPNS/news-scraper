# This is a sample Python script.
from src.parser import parse_articles
from src.scraper import fetch_page
from src.storage import save_to_csv


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    url = 'https://timesofindia.indiatimes.com'
    page_content = fetch_page(url)
    articles = parse_articles(page_content)
    save_to_csv(articles, 'data/raw/articles.csv')
    print('Data saved to articles.csv')


if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
