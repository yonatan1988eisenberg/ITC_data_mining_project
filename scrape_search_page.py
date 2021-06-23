import csv
from http_to_soup import http_to_soup
from tqdm import tqdm

DOMAIN_URL = "https://www.metacritic.com"
MAX_NUM_OF_ARTICLES_PER_PAGE = 100
ARTICLES_TABLE_HEADERS = ["id", "Title", "url"] # todo: add the rest of them


def scrape_search_page(soup, search_url, num_of_articles_to_fetch):
    """
    This function gets a soup and a url to a search page and fetch the first num_of_articles_to_fetch from
    it into a csv file
    :return: True if successful, otherwise False
    """
    articles_fetched = 0

    # open the csv file and write the header
    with open("db.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ARTICLES_TABLE_HEADERS)

        with tqdm(desc='fetching data:', total=num_of_articles_to_fetch) as pbar:
            # while we haven't fetch enough articles, find all the articles in the page
            while articles_fetched < num_of_articles_to_fetch:
                articles = soup.find_all('td', class_='clamp-summary-wrap')
                # for every article in the page, get its url and send to the function which scrape the data from it
                # and than update counter etc
                for article in articles:
                    article_url = article.a.get('href')

                    #scrape_article(file, article_url) todo: add Doron's function

                    articles_fetched += 1
                    pbar.update()
                    if articles_fetched == num_of_articles_to_fetch:
                        return True
                # if we finished the page but need more articles, go to the next page
                pages = soup.find_all('ul', class_="pages").find_all('li')
                for j in range(len(pages)):
                    if pages[j].a is None:
                        next_page = pages[j+1].a.get("href")
                soup = http_to_soup(DOMAIN_URL + next_page)
    return False







