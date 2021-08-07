from get_game_api_data import get_game_api_data
from get_consoles_and_scores import get_consoles_and_scores
from get_soup_general_data import get_soup_general_data


def scrape_game_page(soup, api_header):
    """
    This function gets a game's page soup and scrape it for the details. it returns a dictionary where every key
    is the column. The function also scrapes data from IGNB API using the provided header.
    """

    data = get_soup_general_data(soup)
    data.update(get_consoles_and_scores(soup))
    data.update(get_game_api_data(data['name_of_game'], api_header))

    # todo: handle player perspectives the same way as genres

    return data


#
#     soup_queries = ["soup.find(class_='product_title').h1.get_text()",
#                     "soup.find('span', class_='platform').text.strip()",
#                     "soup.find('div', class_='product_data').find('a').text.strip()",
#                     "soup.find('li', class_='summary_detail release_data').find(class_='data').text",
#                     [soup.find(class_='product_data').find_all(class_='hover_none')[i].text for i in
#                      range(len(soup.find(class_='product_data').find_all(class_='hover_none')))],
#                     "soup.find(class_='metascore_wrap highlight_metascore').find(itemprop='ratingValue').text",
#                     "soup.find(class_='summary').find('a').span.text.strip()",
#                     "(soup.find_all('div', class_='userscore_wrap feature_userscore'))[0].a.text.split()[0]",
#                     "soup.find_all('div', class_='summary')[1].find('a').text.split()[0]",
#                     'soup.find("li", class_="summary_detail developer").find(class_="button").text',
#                     'soup.find("li", class_="summary_detail product_players").find(class_="data").text',
#                     [soup.find_all(class_="details side_details")[1].find(
#                         class_="summary_detail product_genre").find_all(class_="data")[i].text for i in
#                      range(len(soup.find_all(class_="details side_details")[1].find(
#                          class_="summary_detail product_genre").find_all(class_="data")))],
#                     'soup.find(class_="summary_detail product_rating").find(class_="data").text',
#                     "soup.find_all('ol', class_='score_counts hover_none')[0].find_all('li', class_='score_count')[0].find('span', class_='count').text",
#                     "soup.find_all('ol', class_='score_counts hover_none')[0].find_all('li', class_='score_count')[1].find('span', class_='count').text",
#                     "soup.find_all('ol', class_='score_counts hover_none')[0].find_all('li', class_='score_count')[2].find('span', class_='count').text",
#                     "soup.find_all('ol', class_='score_counts hover_none')[1].find_all('li', class_='score_count')[0].find('span', class_='count').text",
#                     "soup.find_all('ol', class_='score_counts hover_none')[1].find_all('li', class_='score_count')[1].find('span', class_='count').text",
#                     "soup.find_all('ol', class_='score_counts hover_none')[1].find_all('li', class_='score_count')[2].find('span', class_='count').text",
#                     ]
#     """
#     def get_consoles_and_scores()
#     returns all the consoles and their scores
#
#     def get_soup_scores(soup/url)
#     returns a dictionary containing the data for
#         'metascore',
#         'number_of_metascore_reviewers',
#         'user_score',
#         'number_of_user_reviews',
#         'critic_review_positive',
#         'critic_review_mixed',
#         'critic_review_negative',
#         'user_review_positive',
#         'user_review_mixed',
#         'user_review_negative'
#
#
#
#
#
#     def sou_general_data(soup)
#     returns a dictionary containing the data for
#         'name_of_game',
#         'publisher',
#         'release_date',
#         'developer',
#         'num_players',
#         'genres',
#         'age_rating',
#
#     def api_data
#
#     def
#     returns a dictionary containing the data for
#         'name_of_game',
#         'main_platform',
#         'release_date',
#         'other_consoles',
#         'metascore',
#         'number_of_metascore_reviewers',
#         'user_score',
#         'number_of_user_reviews',
#         'num_players',
#         'genres',
#
#
#     critic
#     user - ol, score_counts hover_none => li, score_count => span, count.text
#
#     +---------+------------+--------------+-----------+--------------+
# | game_id | console_id | num_positive | num_mixed | num_negative |
# +---------+------------+--------------+-----------+--------------+
# |       2 |          1 | NULL         | 8         | 2            |
# |       2 |          2 | T            | 21        | 1            |
# |       3 |          3 | 64           | 0         | 0            |
# |       3 |          2 | M            | 38        | 2            |
# |       3 |          4 | M            | 86        | 0            |
# |       4 |          5 | 8            | 0         | 0            |
# +---------+------------+--------------+-----------+--------------+
#
#     rules for scores - consoles:
#     * if main console is a link (to the console's page) + there are other consoles (GTA4) =>
#     the scores on this page are main console scores and each console has its own scores
#     * if main console is not a link + there are other consoles (TONY HAWK'S PRO SKATER 2) =>
#     the scores on this page are main console scores and each console has its own scores
#     * if main console is not a link + no other consoles (THE LEGEND OF ZELDA: OCARINA OF TIME) =>
#         the scores on this page are over all scores + console scores
#     * if main console is not a link + there are other consoles =>
#
#
#     """
#     soup_data = []
#     keys = ['name_of_game',
#             'main_platform',
#             'publisher',
#             'release_date',
#             'other_consoles',
#             'metascore',
#             'number_of_metascore_reviewers',
#             'user_score',
#             'number_of_user_reviews',
#             'developer',
#             'num_players',
#             'genres',
#             'age_rating',
#             'critic_review_positive',
#             'critic_review_mixed',
#             'critic_review_negative',
#             'user_review_positive',
#             'user_review_mixed',
#             'user_review_negative'
#             ]
#     # todo: critic/user reviews are not assigning the right values!!!
#     """
#     for unchecked in list_of_scrape_unchecked:
#         if isinstance(unchecked, list):
#             list_of_scrape_checked.append(unchecked)
#
#         else:
#             try:
#                 list_of_scrape_checked.append(eval(unchecked))
#             except:
#                 unchecked = None
#                 list_of_scrape_checked.append(None)
#
#     return list_of_scrape_checked
#     """
#
#     for i in range(len(soup_queries)):
#         if type(soup_queries[i]) == list:
#             soup_data.append(soup_queries[i])
#
#         else:
#             try:
#                 soup_data.append(eval(soup_queries[i]))
#             except:
#                 soup_queries[i] = None
#                 soup_data.append(None)
#
#     row_data = {keys[i]: soup_data[i] for i in range(len(keys))}
#     api_data = get_game_api_data(row_data['name_of_game'], api_header)
#     row_data = {**row_data, **api_data}
#     # row_data | get_game_api_data(row_data['name_of_game'], api_header)
#     # list_of_api_appends = ['franchise_num', 'game_eng_num', 'plr_prspctv_num', 'franchises_name',
#     # 'game_engines_name', 'player_perspectives_name']
#     # for count, i in enumerate(get_game_api_data(row_data['name_of_game'])):
#     #     row_data[list_of_api_appends[count]]= i
#     if row_data['other_consoles']:
#         other_consoles_scores = []
#         consoles_urls = [soup.find(class_='product_data').find_all(class_='hover_none')[i].get('href') for i in
#                          range(len(row_data['other_consoles']))]
#         for url in consoles_urls:
#             other_consoles_scores.append(get_scores_from_soup(url))
#         row_data['other_consoles_scores'] = other_consoles_scores
#
#     return row_data


