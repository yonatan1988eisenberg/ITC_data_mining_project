from http_to_soup import http_to_soup
from tqdm import tqdm
from final_data_scrape import scrape_data

DOMAIN_URL = "https://www.metacritic.com"
FILE_NAME = "db.csv"

def scrape_search_page(search_soup, search_url, num_of_articles_to_fetch):
    """
    This function gets a soup and a url to a search page and fetch the first num_of_articles_to_fetch from
    it into a csv file
    :return: True if successful, otherwise False
    """
    articles_fetched = 0

    # open the csv file and write the header
    with open(FILE_NAME, "w", newline='') as file:
        with tqdm(desc='fetching data', total=num_of_articles_to_fetch) as pbar:
            # while we haven't fetch enough articles, find all the articles in the page
            while articles_fetched < num_of_articles_to_fetch:
                articles = search_soup.find_all('td', class_='clamp-summary-wrap')
                # for every article in the page, get its url and send to the function which scrape the data from it
                # and than update counter etc
                for article in articles:
                    article_url = article.find('a', class_='title')
                    article_url = article_url.get('href')
                    article_soup = http_to_soup(DOMAIN_URL + article_url)
                    if articles_fetched == 0:
                        scrape_data(article_soup).to_csv(file, mode='a', index=False, encoding='utf-8')
                    else:
                        scrape_data(article_soup).to_csv(file, header=False, mode='a', index=False, encoding='utf-8')
                    articles_fetched += 1
                    pbar.update()
                    if articles_fetched == num_of_articles_to_fetch:
                        print("done!, you can find your data at " + FILE_NAME)
                        return
                # if we finished the page but need more articles, go to the next page
                pages = search_soup.find('ul', class_="pages")
                pages = pages.find_all('li')
                for j in range(len(pages) - 1):
                    if pages[j].a is None:
                        next_page = pages[j + 1].a.get("href")
                search_soup = http_to_soup(DOMAIN_URL + next_page)

    print("error scraping!")
    return
