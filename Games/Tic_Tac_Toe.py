import random
from tkinter import *


def write(event):
    if event.keysym == "7":
        next_player(0, 0)
    elif event.keysym == "8":
        next_player(0, 1)
    elif event.keysym == "9":
        next_player(0, 2)
    elif event.keysym == "4":
        next_player(1, 0)
    elif event.keysym == "5":
        next_player(1, 1)
    elif event.keysym == "6":
        next_player(1, 2)
    elif event.keysym == "1":
        next_player(2, 0)
    elif event.keysym == "2":
        next_player(2, 1)
    elif event.keysym == "3":
        next_player(2, 2)
    elif event.keysym == "Return":
        new_game()
    elif event.keysym == "minus":
        quit()
    else:
        print(event.keysym)


def next_player(row, column):
    global player
    global players
    if (buttons[row][column]["text"] != "") is False:

        buttons[row][column]["text"] = player
        if player == players[0]:

            if check_win() is False:
                player = players[1]
                turnShow.config(text=f"{player} turn")

            elif check_win() is True:
                turnShow.config(text=f"{player} win")

        elif player == players[1]:

            if check_win() is False:
                player = players[0]
                turnShow.config(text=f"{player} turn")

            elif check_win() is True:
                turnShow.config(text=f"{player} win")


def check_win():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][2].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][0].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif spaces() == 1:
        return False


def spaces():

    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces != 0:
        return 1
    elif spaces == 0:
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(bg="yellow")
        turnShow.config(text="TIE!")


def new_game():
    global player

    player = random.choice(players)

    turnShow.config(text=f"{player} turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")


window = Tk()
window.bind("<Key>", write)
window.title("X O")

players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

turnShow = Label(window, text=f"{player} turn", font=("", 50))
turnShow.pack(side="top")

reset = Button(window, text="Reset", command=new_game)
reset.pack(side="top")

frame = Frame(window, bg="red", )
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("", 30), width=5, height=2, bg="white",
                                      command=lambda row=row, column=column: next_player(row, column))
        buttons[row][column].grid(row=row, column=column)

print(buttons)
window.mainloop()
