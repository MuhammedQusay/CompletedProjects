from os import system
from time import sleep


tasks: list = []

def show_list():
    system("cls||clear")

    if tasks:
        print(" MY TASKS ".center(50, "#"))
        for no, task in enumerate(tasks, 1):
            print(f"{no}. {task}")
        print("".center(50, "#"))
        print()
        return True

    else:
        return False


def add_task():
    system("cls||clear")

    task_to_add: str = input("Enter the task you want to add: ").strip()

    if task_to_add:
        tasks.append(task_to_add)
        print(f"The task '{task_to_add}' has been successfully added.")
    else:
        print("You entered nothing. Redirecting to the main menu...")
        sleep(3)
        system("cls||clear")



def del_task():
    if not show_list():
        print("There is no tasks to remove.")
        return

    while True:
        try:
            index_to_del: str = input("Please enter the number of the task you want to remove: ").strip()

            if not index_to_del:
                print("You entered nothing. Redirecting to the main menu...")
                sleep(3)
                system("cls||clear")
                break

            index_to_del = int(index_to_del)

            if index_to_del > len(tasks) or index_to_del <= 0:
                print(f"Please enter numbers between 1 and {len(tasks)}.")
                continue

            tasks.pop(index_to_del-1)
            system("cls||clear")
            print(f"Task removed successfully")

            break
        except ValueError:
            print("please enter numbers only.")

def main():
    print("Hello and Welcome to my to-do list app.")

    while True:
        print(" MAIN MENU ".center(50, "="))
        print("1. Show the list.")
        print("2. Add task to the list.")
        print("3. Remove task from the list.")
        print("4. Quit the app.")

        command: str = input("Please enter the number of the command you want to do: ")

        match command:
            case "1":
                if not show_list():
                    print("There is no tasks to show.")
            case "2":
                add_task()
            case "3":
                del_task()
            case "4":
                break
            case _:
                system("cls||clear")
                print("Input invalid, please enter again.")

    system("cls||clear")
    print("Thank you for using my to-do list app :)")


if __name__ == '__main__':
    system("cls||clear")
    main()
    input('Press Enter to quit...')
