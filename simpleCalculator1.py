import time


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def squ(a):
    return a ** 2


def cube(a):
    return a ** 3


def div(a, b):
    if b == 0:
        if a == 0:
            result = "You can't divide Zero by Zero"
        else:
            result = b / a
    else:
        result = a / b

    return result


def main():
    x = None
    while x not in ["1", "2", "3", "4", "5", "6"]:
        x = input("""Which one do you want?
1 for sum
2 for min
3 for multiply
4 for division
5 for square
6 for cube
""")
    if x == "5":
        t = int(input("The number you want: "))
        print()
        print(squ(t))
        print()
    elif x == "6":
        t = int(input("The number you want: "))
        print()
        print(cube(t))
        print()

    else:
        first = float(input("Ok now enter the first number: "))
        second = float(input("Now the second number: "))

        if x == "1":
            print()
            print(f"The result of {first} + {second} is {add(first, second)}")
            print()
        elif x == "2":
            print()
            print(f"The result of {first} - {second} is {sub(first, second)}")
            print()
        elif x == "3":
            print()
            print(f"The result of {first} x {second} is {mult(first, second)}")
            print()
        elif x == "4":
            print()
            if second != 0:
                print(f"The result of {first} / {second} is {div(first, second)}")
            elif second == 0:
                print("You can't divide a number by 0")
            print()

    if ask42():
        return False


def ask42():
    y = None
    while y not in ["1", "2"]:
        y = input("""Do you want to calculate something again?
1 for yes
2 for no
""")
    if y == "1":
        main()
    elif y == "2":
        print("Ok then, thank you to use me, Goodbye")
        time.sleep(2)
        return True


if __name__ == "__main__":
    main()
