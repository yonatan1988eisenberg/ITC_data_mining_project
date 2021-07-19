from configparser import ConfigParser
import argparse

config_object = ConfigParser()
config_object.read("config.ini")


def parse_args():
    """
    This function initialize the parser to the input arguments
    """

    my_parser = argparse.ArgumentParser(description=config_object["PARSER"]["description"])
    my_parser.add_argument('--search_code', '-sc',
                           default=None,
                           type=str,
                           help=config_object["PARSER"]["sc_help"])
    my_parser.add_argument('--fetch', '-f',
                           default=100,
                           type=int,
                           help=config_object["PARSER"]["f_help"])
    my_parser.add_argument('--asc', '-a',
                           default=False,
                           type=bool,
                           help=config_object["PARSER"]["a_help"])
    args = my_parser.parse_args()

    return args
