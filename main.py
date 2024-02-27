from app import start_play, welcome, play_again
from utils import screen_cleaner

response = True

welcome()
while response:
    screen_cleaner()
    start_play()
    response = play_again()
