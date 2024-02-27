from games import memory_game, currency_roulette, guess_game


#"Welcome to the World of Games" message and Name input
def welcome():
    username = input("Enter Username: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


# Function to validate if input is a number within a specified range
def get_valid_input(prompt, range_start, range_end):
    while True:
        try:
            choice = int(input(prompt))
            if range_start <= choice <= range_end:
                return choice
            else:
                print(f"Please enter a number between {range_start} and {range_end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Choose game and difficulty level
def start_play():
    print("""
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for a short duration and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """)
    game_choice = get_valid_input("Enter your choice (1-3): ", 1, 3)

    print("""
    Please choose a difficulty level:
    1. Very Easy
    2. Easy
    3. Medium
    4. Hard
    5. Very Hard
    """)
    difficulty_choice = get_valid_input("Enter your choice (1-5): ", 1, 5)

    if game_choice == 1:
        memory_game.play(difficulty_choice)
    elif game_choice == 2:
        guess_game.play(difficulty_choice)
    elif game_choice == 3:
        currency_roulette.play(difficulty_choice)
    else:
        print("Error: wrong game choice, please choose game between 1-3")

def play_again():
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}

    choice = input("Would you like to play again? [y/n]: ").lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print("Please respond with 'yes' or 'no'")

