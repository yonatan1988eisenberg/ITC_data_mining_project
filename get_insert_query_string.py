def get_insert_query_string(data_dict):
    """
    This function gets a dictionary of columns and values and returns a string and a list of values
    to be used in the query.
    """
    col_string = ""
    vals = []
    for col, val in data_dict.items():
        col_string = col_string + "".join(f"{col}, ")
        vals.append(val)
    col_string = col_string[:-2]
    ph = ('%s, ' * len(vals))[:-2]
    return col_string, vals, ph
