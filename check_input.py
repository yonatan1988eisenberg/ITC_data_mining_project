from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")


def check_input(max_opt):
    """
    This functions asks for the user for input which should be between 0 and max_opt.
    while the input is invalid the user will be asked to reenter a value
    :return:
    """
    while True:
        try:
            user_input = input(config_object['CHECK_INPUT']['CHOICE'])
            if int(user_input) < 0 or int(user_input) > max_opt:
                print(config_object['CHECK_INPUT']['INVALID'])
                continue

            return int(user_input)
        except ValueError:
            print(config_object['CHECK_INPUT']['INVALID'])




