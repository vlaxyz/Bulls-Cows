"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Vlasta Pospěchová
email: pospechovavla@gmail.com
discord: Vlasta P#0037
"""
import random

def generate_secret_number():

    digits = 0
    random_num = 0

    while digits != 4:
        random_num = str(random.randint(1000, 9999))
        digits = len(set([x for x in random_num]))
    return random_num

def evaluate_guess(secret_number, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls += 1
        elif guess[i] in secret_number:
            cows += 1
    return bulls, cows

separator= 47* "-"
print("Hi there!")
print(separator)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print(separator)
print("Enter a number:")
print(separator)
def play_game():
    secret_number = generate_secret_number()
    guesses = 0
    while True:
        guess = input(">>>")
        guesses += 1
        if len(guess) != 4 or not guess.isdigit():
            print("The guess must be a 4 digit number!")
            print(separator)
            continue
        bulls, cows = evaluate_guess(secret_number, guess)
        print(f"{bulls} bulls, {cows} cows")
        print(separator)
        if bulls == 4:
            print(f"Correct, you've guessed the right numberin 4 guesses!")
            break

if __name__ == '__main__':
    play_game()