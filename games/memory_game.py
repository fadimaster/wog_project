import random
import time
from utils import screen_cleaner


def generate_sequence(difficulty_choice):
    random_list = []
    for i in range(0, difficulty_choice):
        random_list.append(random.randint(0, 101))
    return random_list


def get_list_from_user(difficulty_choice):
    while True:
        try:
            user_input = list(map(int, input("Guess numbers: ").split()))
            if len(user_input) == difficulty_choice:
                return user_input
            else:
                print(f"Please enter {difficulty_choice} numbers.")
        except ValueError:
            print("Invalid input.")


def is_list_equal(computer, user):
    computer.sort()
    user.sort()
    return computer == user


def play(difficulty_choice):
    sequence = generate_sequence(difficulty_choice)
    sequence_str = ' '.join(map(str, sequence))
    print(sequence_str, end='', flush=True)
    time.sleep(0.7)  # Wait for 2 seconds
    screen_cleaner(len(sequence_str))
    user_input = get_list_from_user(difficulty_choice)
    result = is_list_equal(sequence, user_input)
    if result:
        print(f"Awesome Memory!!! sequence was {sequence}")
    else:
        print(f"Wrong, sequence was {sequence}")