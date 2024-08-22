import string
from time import sleep
from random import choice

if __name__ == "__main__":
    the_word = "Hello world"
    x = "0"

    for index, letter in enumerate(the_word): 

        while x != letter.lower():

            if letter == " ":
                break

            x = choice(string.ascii_lowercase)
            print(the_word[:index]+x)
            sleep(.05)

