from http_to_soup import http_to_soup
from configparser import ConfigParser

def get_other_consoles_scores(console_urls):
    config_object = ConfigParser()
    config_object.read("config.ini")
    soup = http_to_soup(config_object['USER_QUESTIONS']['DOMAIN_URL'] + console_urls)
    scores_queries = ["soup.find(class_='metascore_wrap highlight_metascore').find(itemprop='ratingValue').text",
                      "soup.find(class_='summary').find('a').span.text.strip()",
                      "(soup.find_all('div', class_='userscore_wrap feature_userscore'))[0].a.text.split()[0]",
                      "soup.find_all('div', class_='summary')[1].find('a').text.split()[0]",
                      'soup.find(class_="summary_detail product_rating").find(class_="data").text',
                      'soup.find_all(class_="count_wrap")[0].find(class_="count").text',
                      'soup.find_all(class_="count_wrap")[1].find(class_="count").text',
                      'soup.find_all(class_="count_wrap")[2].find(class_="count").text',
                      'soup.find_all(class_="count_wrap")[3].find(class_="count").text',
                      'soup.find_all(class_="count_wrap")[4].find(class_="count").text',
                      'soup.find_all(class_="count_wrap")[5].find(class_="count").text'
                      ]
    scores_data = []
    keys = ['metascore',
            'number_of_metascore_reviewers',
            'user_score',
            'number_of_user_reviews',
            'critic_review_positive',
            'critic_review_mixed',
            'critic_review_negative',
            'user_review_positive',
            'user_review_mixed',
            'user_review_negative'
            ]

    for query in scores_queries:
        try:
            scores_data.append(eval(query))
        except:
            scores_data.append(None)

    console_data = {keys[i]: scores_data[i] for i in range(len(keys))}

    return console_data
