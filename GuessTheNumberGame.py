from random import randint
from math import ceil
from os import system


def main() -> None:
    lowest_num, highest_num = get_number_range()

    pc_choice: int = randint(lowest_num, highest_num)

    limit_of_tries: int = ceil((highest_num - lowest_num) ** .5)
    number_of_tries: int = 1

    print(f"\nOk, now I hold a number between {lowest_num} and {highest_num}, try to guess it.")
    print(f"But you have only {limit_of_tries} tries.")

    while True:
        while True:

            player_guess: str = input(f"\nGuess the number ({number_of_tries}/{limit_of_tries}): ")

            if check_if_int(player_guess):
                player_guess: int = int(player_guess)
                break

        if player_guess == pc_choice:
            print()
            print(f"Congratulations! You guessed the number in {number_of_tries} tries out of {limit_of_tries}.".center(
                80, "🥳"))
            break

        elif number_of_tries == limit_of_tries:
            print(f"\nYou've reached the maximum number of guesses. You lost! The number was {pc_choice}.")
            break

        elif player_guess > pc_choice:
            print("\nTry lower.")
        elif player_guess < pc_choice:
            print("\nTry higher.")
        number_of_tries += 1


def get_number_range() -> tuple[int, int]:
    print("From which number to which number you want me to hold?")

    while True:
        lowest_num: str = input("Enter the minimum number: ")
        if check_if_int(lowest_num):
            lowest_num: int = int(lowest_num)
            break

    while True:
        highest_num: str = input("Enter the maximum number: ")
        if check_if_int(highest_num):
            highest_num: int = int(highest_num)
            break

    system("cls||clear")

    if lowest_num == highest_num:
        print("Yeah so funny, select the numbers again.")
        lowest_num, highest_num = get_number_range()

    if lowest_num > highest_num:
        print("Yeah you'r funny, I reversed it.")
        lowest_num, highest_num = highest_num, lowest_num

    return lowest_num, highest_num


def check_if_int(the_num) -> bool:
    try:
        int(the_num)
        return True

    except:
        print("Invalid input. Please input a number.")
        return False


if __name__ == "__main__":
    system("cls||clear")

    print("\n" + "=" * 80)
    print(" WELCOME TO GUESS THE NUMBER GAME! ".center(80, "-"))
    print("=" * 80, "\n")

    print("Hi, let me explain the game to you.\nFirst of all, you will select two numbers for me to hold a number between them, then you will try to guess it. (But don't forget, you have a limited number of tries).\nGood luck. 😉")

    play: str = "y"

    while True:
        if play == "y":
            main()
        elif play == "n":
            system("cls||clear")
            break
        else:
            print("Please enter y or n.")

        play: str = input("\nWould you like to play again? (y/n) ").strip().lower()

    print("#" * 80)
    print(" Thank you for playing! ".center(80, "="))
    print("#" * 80)
    input("Press enter to quit...")
    quit()
