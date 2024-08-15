from os import system


def ask_nums(how_many_nums: int) -> list[float]:
    nums: list[float] = []
    for _ in range(how_many_nums):
        try:
            nums.append(float(input(f"Enter the {'first' if _ == 0 else 'second'} number: ")))
        except ValueError:
            print("Please enter numbers only.")
    return nums


def oparation(selected_oparation: str) -> str:
    try:
        if selected_oparation == "1":
            x, *_, y = ask_nums(2)
            equal: float = x + y

            return f"{x} plus {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_oparation == "2":
            x, *_, y = ask_nums(2)
            equal: float = x - y

            return f"{x} minus {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_oparation == "3":
            x, *_, y = ask_nums(2)
            equal: float = x * y

            return f"{x} times {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_oparation == "4":
            x, *_, y = ask_nums(2)
            equal: float = x / y

            return f"{x} devided by {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_oparation == "5":
            x = ask_nums(1)[0]
            equal: float = x**2
            return f"{x} squared is {equal:10f}".rstrip("0").rstrip(".")

        elif selected_oparation == "6":
            x = ask_nums(1)[0]
            equal: float = x**3
            return f"{x} cubed is {equal:10f}".rstrip("0").rstrip(".")

    except ZeroDivisionError:
        return "You can't devide a number by zero"
    except e as e:
        print(f"error: {e}")


def main() -> None:

    print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Square
6. Cube""")

    while True:
        selected_oparation: str = input("Select an oparation: ")

        if selected_oparation not in ["1", "2", "3", "4", "5", "6"]:
            print("Please type a number between 1 and 6")
            continue

        else:
            break

    system("cls||clear")
    print(oparation(selected_oparation))

    return None


if __name__ == '__main__':
    system("cls||clear")
    print("Welcome to my simple calculator. In this calculator you can add, subtract, multiply, divide, and perform square and cube operations.\nNote: Please try to avoid using very large numbers. It could be too hard for the calculator to calculate, since it is a 'simple' calculator😅")

    again = "y"

    while True:
        if again == "y":
            main()
            continue
        elif again == "n":
            print("Thank you for using me! Goodbye!")
            break
        else:
            print("Please enter 'y' or 'n'")

        again = input("Do you want to calculate something again? (y/n)")

    input("Press enter to quit")
    quit()
