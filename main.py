from app import start_play, welcome, play_again
from utils.utils import screen_cleaner

response = True

username = welcome()
while response:
    screen_cleaner()
    start_play(username)
    response = play_again()
