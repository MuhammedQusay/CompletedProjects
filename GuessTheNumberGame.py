import random
from math import ceil


minX = None
minX = None
playing = True
pc_choice = None
limitOfTries = None
player_guess = None
numberOfTries = None



def from_to():
    print("""
From which number to which number you want me to hold?
          """)

    minX = input("from: ")

    while not checkIfNum1(minX):
        print("Invalid input. Please input a number.")
        minX = input("from: ")
    minX = int(minX)

    maxX = input("to: ")

    while not checkIfNum1(maxX):
        print("Invalid input. Please input a number.")
        maxX = input("to: ")
    maxX = int(maxX)

    if minX == maxX:
        print("\nYeah so funny, select the numbers again.")
        minX, maxX = from_to()
    elif minX > maxX:
        minX, maxX = maxX, minX

    return minX, maxX


def checkIfNum1(thenum):
    try:
        int(thenum)
    except:
        return False
    return True


if __name__ == "__main__":

    print("\n" + "=" * 80)
    print(" WELCOME TO GUESS THE NUMBER GAME! ".center(80, "-"))
    print("=" * 80 , "\n")

    print("Hi, let me explain the game to you.\nFirst of all, you will select two numbers for me to hold a number between them, then you will try to guess it. (But don't forget, you have a limited tries).\nGood luck. 😉")

    while playing:

        minX, maxX = from_to()

        while input(f"\nYou want me to hold a number between {minX} and {maxX}, right? (y/n) ").strip().lower() == "n":
            minX, maxX = from_to()

        pc_choice = random.randint(minX, maxX)

        limitOfTries = ceil((maxX-minX) ** .5)
        numberOfTries = 0

        print(f"\nOk, now I hold a number between {minX} and {maxX}, try to guess it.")
        print(f"But you have only {limitOfTries} tries.")

        while True:
            player_guess = input(f"\nGuess number {numberOfTries+1} out of {limitOfTries}: ")
            while not checkIfNum1(player_guess):
                print("\nEnter a number please,")
                player_guess = input(f"Guess number {numberOfTries+1} out of {limitOfTries}: ")
            player_guess = int(player_guess)

            if player_guess == pc_choice:
                print()
                print(f" Congratulations, you guessed in {numberOfTries+1} out of {limitOfTries} tries.".center(60, "🥳"))
                break
            elif numberOfTries+1 == limitOfTries:
                print(f"\nYou reached the limit of guesses, you lost, the number was {pc_choice}.")
                break
            elif player_guess > pc_choice:
                print("\ntry lower")
            elif player_guess < pc_choice:
                print("\ntry higher")
            numberOfTries += 1

        if input("\nDo you want to play again? (y/n) ").strip().lower() == "n":
            playing = False
    print("#" * 80)
    print(" Thank you for playing! ".center(80, "="))
    print("#" * 80)

