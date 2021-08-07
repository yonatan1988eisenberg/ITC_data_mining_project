def get_exists_query_string(ids_dict):
    """
    This function gets a dictionary of columns and values and returns a string and a list of values
    to search if they exists.
    """
    col_string = ""
    vals = []
    for col, val in ids_dict.items():
        col_string = col_string + "".join(f"CAST({col} as CHAR) LIKE %s AND ")
        vals.append(val)
    col_string = col_string[:-5]
    return col_string, vals
