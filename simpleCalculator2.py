from os import system


def ask_nums(how_many_nums: int) -> list[float]:
    nums: list[float] = []
    for _ in range(how_many_nums):
        try:
            nums.append(float(input(f"Enter the{' ' if how_many_nums == 1 else ' first ' if _ == 0 else ' second '}number: ")))
        except ValueError:
            print("Please enter numbers only.")
    return nums


def operation(selected_operation: str) -> str:
    try:
        if selected_operation == "1":
            x, *_, y = ask_nums(2)
            equal: float = x + y

            return f"{x} plus {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_operation == "2":
            x, *_, y = ask_nums(2)
            equal: float = x - y

            return f"{x} minus {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_operation == "3":
            x, *_, y = ask_nums(2)
            equal: float = x * y

            return f"{x} times {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_operation == "4":
            x, *_, y = ask_nums(2)
            equal: float = x / y

            return f"{x} divided by {y} is {equal:.10f}".rstrip("0").rstrip(".")

        elif selected_operation == "5":
            x = ask_nums(1)[0]
            equal: float = x**2

            return f"{x} squared is {equal:10f}".rstrip("0").rstrip(".")

        elif selected_operation == "6":
            x = ask_nums(1)[0]
            equal: float = x**3

            return f"{x} cubed is {equal:10f}".rstrip("0").rstrip(".")

    except ZeroDivisionError:
        return "You can't divide a number by zero"

    except Exception as e:
        print(f"Error: {e}")


def main() -> None:

    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square\n6. Cube")

    while True:
        selected_operation: str = input("Select an operation: ")

        if selected_operation not in ["1", "2", "3", "4", "5", "6"]:
            print("Please type a number between 1 and 6")
            continue

        else:
            break

    system("cls||clear")
    print(operation(selected_operation))

    return None


if __name__ == '__main__':
    system("cls||clear")
    print("Welcome to my simple calculator. In this calculator you can add, subtract, multiply, divide, and perform square and cube operations.\nNote: Please try to avoid using very large numbers. It could be too hard for the calculator to calculate, since it is a 'simple' calculator😅")

    again = "y"

    while True:
        if again == "y":
            main()

        elif again == "n":
            print("Thank you for using me! Goodbye!")
            break

        else:
            print("Please enter 'y' or 'n'")

        again = input("\nDo you want to calculate something again? (y/n) ").strip().lower()
        system("cls||clear")

    input("Press enter to quit...")
    quit()
