import random



pc_choice = None
player_choice = None

ties = 0
pc_wins = 0
player_wins = 0
roundsPlayed = 0
roundsToPlay = 0


def checkIfNum(num):
    try:
        num = int(num)
    except:
        return False
    return True


def choice(rsp):
    pc_choice = random.randint(0, 2)
    return rsp[pc_choice]


def end(pc_choice, whoWon):
    global pc_wins, player_wins

    if whoWon == "pc":
        print(f"\nPC selected {pc_choice}, you lost.")
        pc_wins += 1

    elif whoWon == "player":
        print(f"\nPC selected {pc_choice}, you won.")
        player_wins += 1


rps = ["Rock", "Paper", "Scissors"]

if __name__ == "__main__":
    print("#" * 80)
    print(" WELCOME TO ROCK PAPER SCISSORS GAME! ".center(80, "-"))
    print("#" * 80)

    print("\nYou know how to play rock paper scissors, I don't need to expalin.")

    roundsToPlay = input("How many rounds you want to play? ")
    while not checkIfNum(roundsToPlay):
        roundsToPlay = input("Invaild input, please enter a number: ")
    roundsToPlay = int(roundsToPlay)

    if roundsToPlay == 0:
        print("You don't want to play?😥")
        print("Ok, get out of here then.")
        input("\npress any key to quit.\n")
        quit()

    while roundsPlayed < roundsToPlay:
        player_choice = input("\n1 for Rock\n2 for Paper\n3 for Scissors\nWhat do you select?\n").strip().lower()
        while player_choice not in ["1", "2", "3"]:
            player_choice = input("\nPlease select one of these '1, 2, 3': ").strip().lower()

        if player_choice == "1":
            player_choice = "Rock"
        elif player_choice == "2":
            player_choice = "Paper"
        elif player_choice == "3":
            player_choice = "Scissors"

        pc_choice = choice(rps)


        if player_choice == pc_choice:
            print(f"\nPC selected {pc_choice} too, it's tie.")
            ties += 1

        elif player_choice == "Rock":
            if pc_choice == "Paper":
                end(pc_choice, "pc")
            else:
                end(pc_choice, "player")

        elif player_choice == "Paper":
            if pc_choice == "Scissors":
                end(pc_choice, "pc")
            else:
                end(pc_choice, "player")

        elif player_choice == "Scissors":
            if pc_choice == "Rock":
                end(pc_choice, "pc")
            else:
                end(pc_choice, "player")

        roundsPlayed += 1

    print(f"\nYou won {player_wins} times. (%{round(player_wins*100/roundsPlayed, ndigits=1)})")
    print(f"PC won {pc_wins} times. (%{round(pc_wins*100/roundsPlayed, ndigits=1)})")
    print(f"And {ties} ties. (%{round(ties*100/roundsPlayed, ndigits=1)})")
    input("press any key to quit.")
    quit()
