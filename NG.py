import random

def get_user_input():
    while True:
        user_input = input("Type a number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print('Please type a valid number.')

def play_number_guessing_game():
    top_of_range = get_user_input()

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        return

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = get_user_input()

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    print("You got it in", guesses, "guesses")

print("Welcome to the Number Guessing Game!")
play_number_guessing_game()
