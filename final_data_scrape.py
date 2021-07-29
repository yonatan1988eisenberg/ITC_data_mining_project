def scrape_data(soup):

    list_of_scrape_unchecked = ["soup.find(class_='product_title').h1.get_text()",
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

    list_of_scrape_checked = []
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

    for i in range(len(list_of_scrape_unchecked)):
        if type(list_of_scrape_unchecked[i]) == list:
            list_of_scrape_checked.append(list_of_scrape_unchecked[i])

        else:
            try:
                list_of_scrape_checked.append(eval(list_of_scrape_unchecked[i]))
            except:
                list_of_scrape_unchecked[i] = None
                list_of_scrape_checked.append(None)

    row_data = {keys[i]: list_of_scrape_checked[i] for i in range(len(keys))}

    return row_data
