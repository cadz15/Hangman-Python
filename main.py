# imports
from os import system
import random

# Variables
WORDS = ("Hello", "Modest", "Instinct",
         "Familiar", "Culture", "Reluctant")
POINTS = 5
MAX_TRIES = 4
MIN_HIDDEN_LETTER = 2

high_score = 0

hidden_letter = []
player_tries = 0
player_score = 0
word_to_guess = WORDS[random.randrange(0, len(WORDS))]


def main():
    print("Welcome to PyHangman!")


def prepare_word(word):
    num_hidden_letter = round(len(word) / 2)
    new_word = ""

    if num_hidden_letter < MIN_HIDDEN_LETTER:
        num_hidden_letter = MIN_HIDDEN_LETTER

    for index, letter in enumerate(word):
        if len(hidden_letter) < num_hidden_letter:
            if len(new_word) < len(word) or new_word[index - 1] != "_":
                if bool(random.getrandbits(1)):
                    new_word += "_"
                    hidden_letter.insert(len(hidden_letter), letter)
                else:
                    new_word += letter
            else:
                new_word += letter
        else:
            new_word += letter

    return new_word


def restore_letter(word, character):
    for index, letter in enumerate(word):
        if word[index] == '_' and word_to_guess[index] == character:
            word[index] = letter

    return word


def check_letter(word, character):
    for letter in hidden_letter:
        if letter == character:
            return True


if __name__ == '__main__':
    main()

