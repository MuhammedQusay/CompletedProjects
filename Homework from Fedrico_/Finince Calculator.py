
from os import system

def calculate(income: float, tax_rate: float, m_or_y: str, names_costs: dict[str, float]) -> None:
    if m_or_y == "m":
        monthly_income: float = income
        yearly_income: float = income * 12
    else:
        yearly_income: float = income
        monthly_income: float = income / 12

    monthly_net_income: float = monthly_income - (monthly_income*tax_rate)
    monthly_net: float = monthly_net_income - sum(names_costs.values())
    yearly_net_income: float = yearly_income - (yearly_income*tax_rate)
    yearly_net: float = yearly_net_income - (sum(names_costs.values())*12)

    print()
    print("SUMMARY".center(80, "="))
    print(f"""
Your monthly income is: {monthly_income:,.2f}
Your monthly income after taxes is: {monthly_net_income:,.2f}
Your monthly net income after taxes and expenses is: {monthly_net:,.2f}

Your yearly income is: {yearly_income:,.2f}
Your yearly income after taxes is: {yearly_net_income:,.2f}
Your yearly net income after taxes and expenses is: {yearly_net:,.2f}
""")
    for name, cost in names_costs.items():
        print(f"You pay {cost:,.2f} monthly and {cost*12:,.2f} yearly for {name}")
    print("".center(80, "="))


def main() -> None:
    print("Hello, today we are gonna calculate your monthly and yearly income and expenses.")

    while True:
        m_or_y: str = input("Do you get paid monthly or yearly? (m/y): ").strip().lower()
        if m_or_y in ["m", "y"]:
            break
        else:
            print("Please enter m or y.")

    while True:
        try:
            income: float = float(input("How much do you get paid (without taxes)? "))

            if income < 0:
                print('How could your "income" be negative 🤦‍♂️')
                continue

            tax_rate: float = float(input("Please enter your tax rate (percentage %): "))/100

            if tax_rate < 0:
                print('How could your tax rate be negative 🤦‍♂️')
                continue

            break

        except ValueError:
            print("Please enter numbers only.")
            continue

    print("Now, let's calculate your monthly expenses.")
    names_costs: dict[str, float] = dict()

    while True:
        the_name: str = input("Please input your the name of the subscription (rent/bills/food/GYM etc) (Enter nothing if you're done): ").strip()

        if the_name == "":
            break

        try:
            the_cost: float = float(input(f"How much do you pay for {the_name}? "))

        except ValueError:
            print("Please enter numbers only.")
            continue

        names_costs[the_name] = the_cost

    calculate(income, tax_rate, m_or_y, names_costs)


if __name__ == "__main__":
    system("cls||clear")
    main()
    input("Press Enter to quit...")
    quit()
