# import only system from os
from os import system, name


SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 1


def screen_cleaner(length=None):
    # clean num of chars
    if length:
        print('\r' + ' ' * length, end='', flush=True)
    # clear all screen
    else:
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
