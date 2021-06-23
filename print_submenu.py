def print_submenu(print_list):
    """
    This function prints a list and asks the user to choose one
    :param print_list: The list with options
    :return: int, representing the user choice
    """
    for index, item in enumerate(print_list):
        print(f"{index}. {item}")
    user_choice = int(input("Please enter your choice:"))

    return int(user_choice)
