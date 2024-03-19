import random


def generate_number(difficulty_choice):
    return random.randint(0, difficulty_choice)


def get_guess_from_user(difficulty_choice):
    while True:
        try:
            choice = int(input(f"Please guess number between 0 and {difficulty_choice}: "))
            if 0 <= choice <= difficulty_choice:
                return choice
            else:
                print(f"Please enter a number between 0 and {difficulty_choice}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def compare_results(computer, user):
    return computer == user


def play(difficulty_choice):
    generated_number = generate_number(difficulty_choice)
    input_number = get_guess_from_user(difficulty_choice)
    result = compare_results(generated_number, input_number)
    if result:
        print(f"Bullseye generated number is {generated_number}")
    else:
        print(f"Incorrect, generated number is {generated_number}")
    return result
