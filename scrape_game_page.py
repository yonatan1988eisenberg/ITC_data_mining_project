from get_game_api_data import get_game_api_data
from get_other_consoles_scores import get_other_consoles_scores


def scrape_game_page(soup, api_header):

    soup_queries = ["soup.find(class_='product_title').h1.get_text()",
                    "soup.find(class_='platform').a.get_text().strip()",
                    "soup.find('div', class_='product_data').find('a').text.strip()",
                    "soup.find('li', class_='summary_detail release_data').find(class_='data').text",
                    [soup.find(class_='product_data').find_all(class_='hover_none')[i].text for i in
                     range(len(soup.find(class_='product_data').find_all(class_='hover_none')))],
                    "soup.find(class_='metascore_wrap highlight_metascore').find(itemprop='ratingValue').text",
                    "soup.find(class_='summary').find('a').span.text.strip()",
                    "(soup.find_all('div', class_='userscore_wrap feature_userscore'))[0].a.text.split()[0]",
                    "soup.find_all('div', class_='summary')[1].find('a').text.split()[0]",
                    'soup.find("li", class_="summary_detail developer").find(class_="button").text',
                    'soup.find("li", class_="summary_detail product_players").find(class_="data").text',
                    [soup.find_all(class_="details side_details")[1].find(
                        class_="summary_detail product_genre").find_all(class_="data")[i].text for i in
                     range(len(soup.find_all(class_="details side_details")[1].find(
                         class_="summary_detail product_genre").find_all(class_="data")))],
                    'soup.find(class_="summary_detail product_rating").find(class_="data").text',
                    'soup.find_all(class_="count_wrap")[0].find(class_="count").text',
                    'soup.find_all(class_="count_wrap")[1].find(class_="count").text',
                    'soup.find_all(class_="count_wrap")[2].find(class_="count").text',
                    'soup.find_all(class_="count_wrap")[3].find(class_="count").text',
                    'soup.find_all(class_="count_wrap")[4].find(class_="count").text',
                    'soup.find_all(class_="count_wrap")[5].find(class_="count").text'
                    ]

    soup_data = []
    keys = ['name_of_game',
            'main_platform',
            'publisher',
            'release_date',
            'other_consoles',
            'metascore',
            'number_of_metascore_reviewers',
            'user_score',
            'number_of_user_reviews',
            'developer',
            'num_players',
            'genres',
            'age_rating',
            'critic_review_positive',
            'critic_review_mixed',
            'critic_review_negative',
            'user_review_positive',
            'user_review_mixed',
            'user_review_negative'
            ]
    """    
    for unchecked in list_of_scrape_unchecked:
        if isinstance(unchecked, list):
            list_of_scrape_checked.append(unchecked)

        else:
            try:
                list_of_scrape_checked.append(eval(unchecked))
            except:
                unchecked = None
                list_of_scrape_checked.append(None)

    return list_of_scrape_checked
    """

    for i in range(len(soup_queries)):
        if type(soup_queries[i]) == list:
            soup_data.append(soup_queries[i])

        else:
            try:
                soup_data.append(eval(soup_queries[i]))
            except:
                soup_queries[i] = None
                soup_data.append(None)

    row_data = {keys[i]: soup_data[i] for i in range(len(keys))}
    api_data = get_game_api_data(row_data['name_of_game'], api_header)
    row_data = {**row_data, **api_data}
    # row_data | get_game_api_data(row_data['name_of_game'], api_header)
    # list_of_api_appends = ['franchise_num', 'game_eng_num', 'plr_prspctv_num', 'franchises_name',
    # 'game_engines_name', 'player_perspectives_name']
    # for count, i in enumerate(get_game_api_data(row_data['name_of_game'])):
    #     row_data[list_of_api_appends[count]]= i
    if row_data['other_consoles'] is not None:
        other_consoles_scores = []
        consoles_urls = [soup.find(class_='product_data').find_all(class_='hover_none')[i].get('href') for i in
                         range(len(row_data['other_consoles']))]
        for url in consoles_urls:
            other_consoles_scores.append(get_other_consoles_scores(url))

    return row_data


