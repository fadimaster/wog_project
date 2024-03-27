from os import name
from subprocess import call

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1
SCORES_HTML_FILE = "scores.html"
ERROR_HTML_FILE = "error.html"


def screen_cleaner(length=None):
    # clear num of chars
    if length:
        print('\r' + ' ' * length, end='', flush=True)
    # clear the entire screen
    else:
        _ = call('clear' if name == 'posix' else 'cls')
