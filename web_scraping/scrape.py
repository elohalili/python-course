import pprint

import requests
from bs4 import BeautifulSoup

# web scraping
# get news from hacker news with a score higher than 100


def get_hn_page_content(page=1):
    hacker_news_url = f'https://news.ycombinator.com/news?p={page}'
    res = requests.get(hacker_news_url)
    # parse the html page into BeautifulSoup obj
    return BeautifulSoup(res.text, 'html.parser')


def get_news_list(soup):
    # extract a cleaned list of rows in the page's table
    tr_list = [tr for tr in soup.select('.itemlist tr')
               if not ('class' in tr.attrs and ('spacer' in tr['class'] or 'morespace' in tr['class']))]
    # remove last item (next page tr)
    tr_list.pop()

    news_list = []

    # iterate the rows in pair due to data structure
    # 1° tr -> title and link
    # 2° tr -> score
    i = 0
    while i < len(tr_list):
        tr_title = tr_list[i]
        tr_score = tr_list[i+1]

        title_elem = tr_title.find('a', {'class': 'storylink'})
        title = title_elem.text
        link = title_elem['href']

        score = int(
            tr_score.find('span', {'class': 'score'}).text.replace(' points', ''))

        if score > 100:
            news_list.append({'title': title, 'link': link, 'score': score})
        i += 2
    return news_list


def sort_news_by_score(list):
    # sort by the score passing the lambda function to assign the right key
    return sorted(list, key=lambda k: k['score'], reverse=True)


def get_hn_news(pages):
    news_list = []
    for page in range(pages):
        content = get_hn_page_content(page+1)
        news_list += get_news_list(content)
    return sort_news_by_score(news_list)


pprint.pprint(get_hn_news(2))
