import string
from time import sleep
from random import choice


if __name__ == "__main__":
    the_real_word: str = input('What word do you want to me to type in a cool way? ("Hello world" for example)\n')
    the_random_word: list = list()

    for i in the_real_word:
        the_random_word.append(choice(string.ascii_lowercase) if i != " " else " ")


    while not (list(the_real_word) == the_random_word):

        for index, letter in enumerate(the_real_word):

            if letter.lower() == the_random_word[index].lower():

                the_random_word[index]: str = letter
                continue

            the_random_word[index]: str = choice(string.ascii_lowercase)


        print("".join(the_random_word), end="\r")
        sleep(.1)

    print(the_real_word)
