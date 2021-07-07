def config_use_dict(config_item):
    dict_list = []
    str_to_lst = config_item.split(',')
    for i in str_to_lst:
        dict_list.append(i.strip("][ '"))

    return dict_list

