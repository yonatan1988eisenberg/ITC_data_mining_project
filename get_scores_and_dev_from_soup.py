def get_scores_and_dev_from_soup(soup):
    """
    This function gets a soup and returns a dictionary containing all the available scores and the developer
    from that soup
    """
    data_dict = {}

    # metascore and number_of_metascore_reviewers
    meta_wrap = soup.find('div', class_='metascore_wrap highlight_metascore')
    if meta_wrap:
        meta_wrap.find('span', itemprop='ratingValue')
        if meta_wrap:
            data_dict['number_of_metascore_reviewers'] = meta_wrap.find('div', class_='summary').a.span.text.strip()
            data_dict['metascore'] = meta_wrap.find('span', itemprop='ratingValue').text

    # user_score and number_of_user_reviews
    user_wrap = soup.find('div', class_='userscore_wrap feature_userscore')
    if user_wrap and user_wrap.find('div', class_='metascore_w user large game positive'):
        data_dict['user_score'] = user_wrap.find('div', class_='metascore_w user large game positive').text
        data_dict['number_of_user_reviews'] = user_wrap.find('span', class_='count').a.text.split()[0]

    # critics detailed scores
    critic_detailed_wrap = soup.find('div', class_='module reviews_module critic_reviews_module')
    if critic_detailed_wrap:
        critic_detailed_wrap = critic_detailed_wrap.find_all('li', class_='score_count')
        scores = [score.find('span', class_='count').text for score in critic_detailed_wrap]
        if scores:
            data_dict['critic_review_positive'] = scores[0]
            data_dict['critic_review_mixed'] = scores[1]
            data_dict['critic_review_negative'] = scores[2]

    # users detailed scores
    users_detailed_wrap = soup.find('div', class_='module reviews_module user_reviews_module')
    if users_detailed_wrap:
        users_detailed_wrap = users_detailed_wrap.find_all('li', class_='score_count')
        scores = [score.find('span', class_='count').text for score in users_detailed_wrap]
        if scores:
            data_dict['user_review_positive'] = scores[0]
            data_dict['user_review_mixed'] = scores[1]
            data_dict['user_review_negative'] = scores[2]

    # developer
    dev = soup.find("li", class_="summary_detail developer")
    if dev:
        data_dict['developer'] = dev.find(class_="button").text

    return data_dict
