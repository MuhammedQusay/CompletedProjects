# From 2025 me to 2023 me: Bro, who wrote this code? I hope it wasn’t me.
from tkinter import *


def a(event):

    NUMS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    dict_of_foos: dict[str: str] = {"plus": "+",
                                    "minus": "-",
                                    "slash": "/",
                                    "asterisk": "*",
                                    "period": "."}

    if event.keysym in NUMS:
        write(event.keysym)

    elif event.keysym in dict_of_foos:
        write(dict_of_foos[event.keysym])

    elif event.keysym == "Return":
        equals()
    elif event.keysym == "c":
        clear()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        quit()


def write(x):
    global eq_txt
    if eq_txt == "ERROR" or eq_txt == "Can't divide by 0":
        eq_txt = ""
    eq_txt = eq_txt + x
    the_shower.config(text=eq_txt)


def equals():
    global eq_txt
    try:
        if eq_txt == "ERROR" or eq_txt == "":
            eq_txt = "0"
        eq_txt = str(eval(eq_txt))
        numof0 = 0
        if "." in list(eq_txt):
            dot = eq_txt.find(".")
            for i in list(eq_txt[dot:]):
                if i == "0":
                    numof0 += 1
                    if numof0 == 5:
                        eq_txt = eq_txt[:dot+numof0]
                        equals()
        if eq_txt[-2:] == ".0":
            eq_txt = eq_txt[:-2]
    except ZeroDivisionError:
        eq_txt = "Can't divide by 0"
    except SyntaxError:
        eq_txt = "ERROR"
    the_shower.config(text=eq_txt)


def clear():
    global eq_txt
    eq_txt = ""
    the_shower.config(text=eq_txt)


def backspace():
    global eq_txt
    a = list(eq_txt)
    eq_txt = eq_txt[:-1]
    the_shower.config(text=eq_txt)


if __name__ == "__main__":

    window = Tk()
    window.config(bg="#b3c1a4")
    window.geometry("800x500")

    window.bind("<Key>", a)

    eq_txt = ""

    the_shower = Label(window, width=13, bg="#b3c7c4", font=("", 50), )
    the_shower.pack()

    buttons_frame = Frame(window, bg="green", )
    buttons_frame.pack()

    numbut = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0]]

    for row in range(len(numbut)):
        for col in range(len(numbut[row])):
            numbut[row][col] = Button(buttons_frame, bg="#34ebcf", text="X",
                                      activebackground="black",
                                      width=7, height=2, font=("", 20))
            numbut[row][col].grid(row=row, column=col)

    numbut[0][0].config(text="/", command=lambda: write("/"))
    numbut[0][1].config(text="*", command=lambda: write("*"))
    numbut[0][2].config(text="-", command=lambda: write("-"))
    numbut[0][3].config(text="+", command=lambda: write("+"))
    numbut[1][0].config(text="7", command=lambda: write("7"))
    numbut[1][1].config(text="8", command=lambda: write("8"))
    numbut[1][2].config(text="9", command=lambda: write("9"))
    numbut[1][3].config(text=",", command=lambda: write("."))
    numbut[2][0].config(text="4", command=lambda: write("4"))
    numbut[2][1].config(text="5", command=lambda: write("5"))
    numbut[2][2].config(text="6", command=lambda: write("6"))
    numbut[2][3].config(text="=", command=equals)
    numbut[3][0].config(text="1", command=lambda: write("1"))
    numbut[3][1].config(text="2", command=lambda: write("2"))
    numbut[3][2].config(text="3", command=lambda: write("3"))
    numbut[3][3].config(text="C", command=clear)
    numbut[4][0].config(text="0", command=lambda: write("0"))

    window.mainloop()
