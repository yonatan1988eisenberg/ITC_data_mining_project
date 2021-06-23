def check_input(max_opt):
    """
    This functions asks for the user for input which should be between 0 and max_opt.
    while the input is invalid the user will be asked to reenter a value
    :return:
    """
    while True:
        try:
            user_input = input("Please enter your choice:")
            if int(user_input) < 0 or int(user_input) > max_opt:
                print("Invalid integer was given")
                continue

            return int(user_input)
        except ValueError:
            print("Invalid integer was given")




