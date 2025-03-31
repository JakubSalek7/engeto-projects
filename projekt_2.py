"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Salek
email: jakub.n.salek@gmail.com
discord: zob3772
"""

import random
import time

def generate_secret_number():
    """Vygeneruje náhodné 4místné číslo s unikátními číslicemi a nezačínající nulou."""
    digits = list(range(1, 10)) + [0]
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def validate_input(user_input):
    """Validuje vstup od uživatele."""
    if len(user_input) != 4 or not user_input.isdigit():
        return False
    if user_input[0] == '0':
        return False
    if len(set(user_input)) != 4:
        return False
    return True

def evaluate_guess(secret, guess):
    """Vyhodnotí počet bulls a cows."""
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def main():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)
    
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()
    
    while True:
        guess = input("Enter a number: ")
        print("-" * 47)
        
        if not validate_input(guess):
            print("Invalid input! Please enter a unique 4-digit number not starting with 0.")
            print("-" * 47)
            continue
        
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        
        if bulls == 4:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"Time taken: {elapsed_time} seconds.")
            print("-" * 47)
            break
        
        bulls_word = "bull" if bulls == 1 else "bulls"
        cows_word = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bulls_word}, {cows} {cows_word}")
        print("-" * 47)

if __name__ == "__main__":
    main()
