import requests


def get_money_interval():
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/98a01502c7523d8f777da41b/pair/USD/ILS'

    # Making our request
    response = requests.get(url)
    data = response.json()

    # Your JSON object
    return data.get("conversion_rate")


def get_guess_from_user():
    while True:
        try:
            choice = float(input(f"Please guess USD to ILS rate: "))
            if 1 <= choice <= 100:
                return choice
            else:
                print(f"Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def compare_results(difficulty_choice, computer, user):
    rate_delta = abs(computer - user)
    if difficulty_choice == 1:
        return rate_delta <= 0.50
    elif difficulty_choice == 2:
        return rate_delta <= 0.40
    elif difficulty_choice == 3:
        return rate_delta <= 0.30
    elif difficulty_choice == 4:
        return rate_delta <= 0.20
    elif difficulty_choice == 5:
        return rate_delta <= 0.10


def play(difficulty_choice):
    rate = get_money_interval()
    user_input = get_guess_from_user()
    result = compare_results(difficulty_choice, rate, user_input)
    if result:
        print(f"Correct the rate is {rate}")
    else:
        print(f"Wrong the rate is {rate} you guessed {user_input}")
    return result
