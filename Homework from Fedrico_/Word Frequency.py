from collections import Counter
import re

def get_frequency(text: str, most_common: int) -> list[tuple[str, int]]:
    words: list = re.findall(r"\b\w+\b", text)
    counted_words = Counter(words).most_common(most_common)
    return counted_words




def main():
    text = input("Input the text: ").strip()

    if not text:
        print("No text entered, exiting...")
        return

    while True:
        most_common: str = input("How many words you want to see? ")

        if most_common.isdigit():
            most_common = int(most_common)
            break

        else:
            print("Please enter numbers only.")

    word_frequencies = get_frequency(text, most_common)

    print(f"These are the {most_common} most common words:")
    for word, count in word_frequencies:
        print(f"The word '{word}' is typed {count} times")



if __name__ == '__main__':
    main()
    input('Press Enter to quit...')
