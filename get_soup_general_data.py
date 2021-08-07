def get_soup_general_data(soup):
    """
    This function gets a game's soup and returns a dictionary containing general data about the game
    """
    data_dict = {}

    name = soup.find(class_='product_title')
    if name:
        data_dict['name_of_game'] = name.h1.text

    pub = soup.find('li', class_='summary_detail publisher')
    if pub:
        data_dict['publisher'] = pub.a.text.strip()

    rel_date = soup.find('li', class_='summary_detail release_data')
    if rel_date:
        rel_date = rel_date.find('span', class_='data')
        if rel_date:
            data_dict['release_date'] = rel_date.text.strip()

    num_p = soup.find("li", class_="summary_detail product_players")
    if num_p:
        data_dict['num_players'] = num_p.find(class_="data").text

    genres = soup.find("li", class_='summary_detail product_genre')
    if genres:
        genres = genres.find_all('span', class_='data')
        data_dict['genres'] = [genre.text for genre in genres]

    age = soup.find("li", class_="summary_detail product_rating")
    if age:
        data_dict['age_rating'] = age.find('span', class_="data").text

    return data_dict
