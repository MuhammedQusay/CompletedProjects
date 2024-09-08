import string
from time import sleep
from random import choice


if __name__ == "__main__":
    the_word = input('What word do you want to me to type in a cool way? ("Hello world" for example)\n')
    rand_letter: str = choice(string.ascii_lowercase)

    for index, letter in enumerate(the_word): 

        while x != letter.lower():

            if letter == " ":
                break

            rand_letter: str = choice(string.ascii_lowercase)
            print(the_word[:index]+x)
            sleep(.05)
