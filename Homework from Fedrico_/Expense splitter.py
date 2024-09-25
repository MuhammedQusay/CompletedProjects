def main():
    while True:
        try:
            total_money: float = float(input("Enter the amount of the money you want to split: "))
            num_of_people: int = int(input("Enter the number of the people you want to split: "))

            if total_money == 0:
                print("I don't think there is money to split.")
                break

            if num_of_people > 1:
                print("Ok, then...")
                print(f"Everyone going to pay {(total_money/num_of_people):,.2f}.")
                break
            elif num_of_people == 1:
                print("Are you joking? You can't split money with yourself. I think you gonna pay it all haha, lonely.")
                print(f"It's {total_money:,.2f} BTW.")
                break
            elif num_of_people <= 0 or total_money < 0:
                print("I think you entered somthing wrong, lets try again.")
                continue

        except ValueError:
            print("Please enter numbers only.")


if __name__ == '__main__':

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

    input("Press enter to quit...")
    quit()
