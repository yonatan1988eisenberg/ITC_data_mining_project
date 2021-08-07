from check_input import check_input


def print_submenu(string_list):
    """
    This function prints a list and asks the user to choose one, it than verifies the input (via check_input function)
    :param string_list: The list of options, if it's a string it will be casted to a list
    :return: int, representing the user choice
    """

    if type(string_list) == str:
        print_list = string_list.strip('][').split(', ')
    else:
        print_list = string_list

    for index, item in enumerate(print_list):
        print(f"{index}. {item}")

    user_choice = check_input(len(print_list) - 1)

    return int(user_choice)

