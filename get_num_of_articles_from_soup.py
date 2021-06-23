from http_to_soup import http_to_soup
MAX_ARTICLES_PER_PAGE = 100
DOMAIN_URL = "https://www.metacritic.com"
GAMES_URL = "/game"


def get_num_of_articles_from_soup(soup):

    max_pages = soup.find('li', class_="page last_page")
    if max_pages is None:
        articles = soup.find_all('td', class_='clamp-summary-wrap')
        return len(articles)
    else:
        max_page_url = DOMAIN_URL + max_pages.a.get('href')
        soup = http_to_soup(max_page_url)
        articles = soup.find_all('td', class_='clamp-summary-wrap')
        return len(articles) + (int(max_pages.a.text) * MAX_ARTICLES_PER_PAGE)

