
import random
from os import system


def main() -> None:
    num_of_fails: int = 0
    tried_chars: str = " ()"
    won = False

    word: str = select_a_word()
    showed_word: list[str] = ["_"] * len(word)

    while num_of_fails < 6:
        show_the_man(num_of_fails)
        showed_word: list[str] = show_word_progress(word, tried_chars, showed_word)

        if not "_" in showed_word:
            won = True
            break

        input_char: str = input("Try to guess a letter: ").strip().lower()
        system("cls||clear")
        if not input_char:
            continue

        for char in input_char:

            if char == "?":
                print(f"You tried '{tried_chars[3:]}', you have {6-num_of_fails} fails.")
                continue

            if char in tried_chars:
                print("You already tried this letter.")
                continue

            tried_chars += char

            if not check_the_char(char, word):
                num_of_fails += 1

    system("cls||clear")
    show_the_man(num_of_fails)
    show_word_progress(word, tried_chars, showed_word)
    if won:
        print("YOU WON, you saved the man!!!")
    else:
        print(f"You lost, the word was '{word}'.")


def check_the_char(char: str, word: str) -> bool:
    return True if char in word.lower() else False


def select_a_word() -> str:

    words = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates (UAE)', 'United Kingdom (UK)', 'United States of America (USA)', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

    return random.choice(words)

    # try:
    #     with open("WordsForHangManGame.txt", "r") as f:
    #         lines: list[str] = f.readlines()
    #         line_no: int = random.randint(0, len(lines))
    #         return lines[line_no - 1].strip()

    # except FileNotFoundError as e:
    #     print("Sorry, the file of the words has not been found.")


def show_the_man(num_of_fails: int) -> None:
    if num_of_fails == 0:
        print("""
   ____________
   |          |
   |          |
   |
   |
   |
   |
   |
 __|__
              """)
    elif num_of_fails == 1:
        print("""
   ____________
   |          |
   |          |
   |          O
   |
   |
   |
   |
 __|__
""")
    elif num_of_fails == 2:
        print("""
   ____________
   |          |
   |          |
   |          O
   |          |
   |
   |
   |
 __|__
""")
    elif num_of_fails == 3:
        print("""
   ____________
   |          |
   |          |
   |          O
   |          |\\
   |
   |
   |
 __|__
""")
    elif num_of_fails == 4:
        print("""
   ____________
   |          |
   |          |
   |          O
   |         /|\\
   |
   |
   |
 __|__
""")
    elif num_of_fails == 5:
        print("""
   ____________
   |          |
   |          |
   |          O
   |         /|\\
   |         /
   |
   |
 __|__
""")
    elif num_of_fails == 6:
        print("""
   ____________
   |          |
   |          |
   |          O
   |         /|\\
   |         / \\
   |
   |
 __|__
              
You killed the man!!
""")


def show_word_progress(word: str, tried_chars: str, showed_word: list[str]) -> list[str]:

    for i in range(len(word)):
        if word[i].lower() in tried_chars:
            showed_word[i] = word[i]

    print(" ".join(showed_word))

    return showed_word


if __name__ == "__main__":

    system("cls||clear")
    print("""Welcome to the HangMan Game!""")

    rules: str = ""
    play_again: str = "y"

    while True:
        rules = input("Do you know how to play the game? (y/n) ").strip().lower()
        system("cls||clear")

        if rules == "n":
            input("In this game, there is a hunged man and a secret word, and your job is to know what is the word by guessing the letters of it. If you guess the word correctly, the man lives, if you don't, he dies!!\n\nPress enter to continue...")
            system("cls||clear")
            break
        elif rules == "y":
            break
        else:
            print("Please enter 'y' or 'n'.")


    print("In case you didn't know, you can type '?' if you want to know what letters did you try and how many lives you have.")

    while True:
        if play_again == "y":
            main()
        elif play_again == "n":
            print("Thank you for playing.")
            input("Press enter to quit...")
            quit()
        else:
            print("Please enter 'y' or 'n'.")

        play_again = input("\nDo you want to play again? (y/n) ")
        system("cls||clear")