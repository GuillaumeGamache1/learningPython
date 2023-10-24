#This is a number guessing game. In this project I learned about random

import random

num1 = 0
num2 = 0
answer = 0
good_guess = False
number_guessed = 0
ranNum = 0


def generate_random_number(low, high):
    ranNum = random.randint(low, high)
    return ranNum

def compare_number(ans, num, good_guess):
    if ans < num:
        print("Too low!")
        good_guess = False
        return good_guess
    elif ans > num:
        print("Too high")
        good_guess = False
        return good_guess
    else:
        print("You got it!")
        good_guess = True
        return good_guess

def ask_number():
    while True:
        num1 = input("Enter the lowest number: " + '\n')

        try:
            num1=int(num1)
            break
        except ValueError:
            print('\n' + "Please eneter a valid number" + '\n')

    while True:    
        num2 = input("Enter the highest number: " + '\n')

        try:
            num2=int(num2)
            return num1, num2
        except ValueError:
            print('\n' + "Please eneter a valid number" + '\n')

        
def guess():
    while True:
        guess = input("Now guess the number I'm thinking of: " + '\n')

        try:
            number_guessed = int(guess)
            return number_guessed
        except ValueError:
            print("Please enter a number")

num1, num2 = ask_number()
ranNum = generate_random_number(num1, num2)
number_guessed = guess()

while not good_guess:
    number_guessed = guess()
    good_guess = compare_number(number_guessed, ranNum, good_guess)

    if good_guess:
        break


# 1 erreurs: 1. Quand je demande au user d'enter un guess, ca ne le compare pas et fait juste lui re-demander de le rentrer une deuxieme fois.
            

