import pandas as pd


def scrape_data(soup):
    """
    This function gets a soup to an article page and scrape it for data
    :return: a pandas.dataframe object, containing all the scraped data
    """
    # try:
    #     name_of_game = [(soup.find(class_="product_title")).h1.get_text()]
    # except:
    #     name_of_game = None

    name_of_game = None if soup.find(class_="product_title") is None \
        else (soup.find(class_="product_title")).h1.get_text()

    try:
        main_platform = [(soup.find(class_="platform")).a.get_text().strip()]
    except:
        main_platform = None

    try:
        publisher = [soup.find('div', class_='product_data').find('a').text.strip()]
    except:
        publisher = None

    try:
        release_date_initial = soup.find(class_="summary_detail release_data")
    except:
        release_date_initial = None

    try:
        release_date = list(release_date_initial.children)[3].get_text()
    except:
        release_date = None

    try:
        other_consoles_initial = soup.find('li', class_='summary_detail product_platforms').find_all('a')
    except:
        other_consoles_initial = None

    try:
        other_consoles = [[i.text for i in other_consoles_initial]]
    except:
        other_consoles = None

    try:
        metascore = soup.find(class_='metascore_anchor').text.split()
    except:
        metascore = None

    try:
        number_of_metascore_reviewers = [soup.find(class_='count').find('a').text.split()[0]]
    except:
        number_of_metascore_reviewers = None

    try:
        user_score = (soup.find_all('div', class_='userscore_wrap feature_userscore'))[0].a.text.split()
    except:
        user_score = None

    try:
        number_of_user_reviews = [soup.find_all('div', class_='summary')[1].find('a').text.split()[0]]
    except:
        number_of_user_reviews = None

    try:
        developer = [soup.find('li', class_="summary_detail developer").find(class_='button').text]
    except:
        developer = None

    try:
        initial_genres = [i for i in soup.find('li', class_='summary_detail product_genre').text.split()]
        genres = [initial_genres[1:]]
    except:
        genres = None

    try:
        num_players = [soup.find('li', class_="summary_detail product_players").find(class_='data').text]
    except:
        num_players = None

    try:
        age_rating = [soup.find(class_='summary_detail product_rating').find(class_='data').text]
    except:
        age_rating = None

    try:
        critic_review_setup = soup.find_all('div', class_='count_wrap')
    except:
        critic_review_setup = None

    try:
        critic_review_positive_initial = list(critic_review_setup)[0]
    except:
        critic_review_positive_initial = None

    try:
        critic_review_positive = [critic_review_positive_initial.find(class_='count').text]
    except:
        critic_review_positive = None

    try:
        critic_review_mixed_initial = list(critic_review_setup)[1]
    except:
        critic_review_mixed_initial = None

    try:
        critic_review_mixed = [critic_review_mixed_initial.find(class_='count').text]
    except:
        critic_review_mixed = None

    try:
        critic_review_negative_initial = list(critic_review_setup)[2]
    except:
        critic_review_negative_initial = None

    try:
        critic_review_negative = [critic_review_negative_initial.find(class_='count').text]
    except:
        critic_review_negative = None

    try:
        user_review_positive_initial = list(critic_review_setup)[3]
    except:
        user_review_positive_initial = None

    try:
        user_review_positive = [user_review_positive_initial.find(class_='count').text]
    except:
        user_review_positive = None

    try:
        user_review_mixed_initial = list(critic_review_setup)[4]
    except:
        user_review_mixed_initial = None

    try:
        user_review_mixed = [user_review_mixed_initial.find(class_='count').text]
    except:
        user_review_mixed = None

    try:
        user_review_negative_initial = list(critic_review_setup)[5]
    except:
        user_review_negative_initial = None

    try:
        user_review_negative = [user_review_negative_initial.find(class_='count').text]
    except:
        user_review_negative = None

    data = pd.DataFrame({
        'name_of_game': name_of_game,
        'main_platform': main_platform,
        'publisher': publisher,
        'release_date': release_date,
        'other_consoles': other_consoles,
        'metascore': metascore,
        'number_of_metascore_reviewers': number_of_metascore_reviewers,
        'number_of_user_reviews': number_of_user_reviews,
        'user_score': user_score,
        'Developer': developer,
        'genres': genres,
        'num_players': num_players,
        'age_rating': age_rating,
        'critic_review_positive': critic_review_positive,
        'critic_review_mixed': critic_review_mixed,
        'critic_review_negative': critic_review_negative,
        'user_review_positive': user_review_positive,
        'user_review_mixed': user_review_mixed,
        'user_review_negative': user_review_negative,
    })

    return data
