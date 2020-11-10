# imports
from os import system
import random

# Variables
WORDS = ("hello", "modest", "instinct",
         "familiar", "culture", "reluctant")
POINTS = 5
MAX_TRIES = 4
MIN_HIDDEN_LETTER = 2

hidden_letter = []


def main():
    high_score = 0

    player_guess_letter = []
    player_tries = 0
    player_score = 0

    choice = ''

    while choice != "exit":
        is_complete = False
        word_to_guess = WORDS[random.randrange(0, len(WORDS))]

        print(f"Welcome to Python Hangman! \t\t\t\t High Score : {high_score}")
        choice = input("Press 'p' to play the game! \n")
        print(choice)
        if choice.lower() == 'p':
            player_guess_letter.clear()
            word_to_complete = prepare_word(word_to_guess)
            player_tries = 0

            while not is_complete:
                clean_screen()  # Not working in Pycharm "run console".

                print(f"Word To Guess \t\t\t\t\t\t\t Score : {player_score}")
                print(f"\t\t\t\t {word_to_complete} \t\t\t\t Tries left: {MAX_TRIES - player_tries}")
                print(f"Wrong guess : {display_wrong_choice(player_guess_letter)}")
                guess_letter = input("Enter a letter : ").lower()

                if check_letter(guess_letter, hidden_letter):
                    hidden_letter.remove(guess_letter)
                    word_to_complete = restore_letter(word_to_guess, word_to_complete, guess_letter)
                    player_score += POINTS
                    if player_score > high_score:
                        high_score = player_score
                else:
                    if len(hidden_letter) > 0:
                        if not check_letter(guess_letter, player_guess_letter):
                            player_guess_letter.insert(len(player_guess_letter), guess_letter)
                            player_tries += 1

                if player_tries > 4 or len(hidden_letter) == 0:
                    is_complete = True


def prepare_word(word):
    num_hidden_letter = round(len(word) / 2)
    new_word = ""
    hidden_letter.clear()

    if num_hidden_letter < MIN_HIDDEN_LETTER:
        num_hidden_letter = MIN_HIDDEN_LETTER

    for index, letter in enumerate(word):
        not_hidden = True
        if len(hidden_letter) < num_hidden_letter:
            if len(new_word) < len(word) or new_word[index - 1] != "_":
                if bool(random.getrandbits(1)):
                    new_word += "_"
                    hidden_letter.insert(len(hidden_letter), letter)
                    not_hidden = False
        if not_hidden:
            new_word += letter

    return new_word


def restore_letter(word_to_guess, word, character):
    new_word = ''
    for index, letter in enumerate(word):
        if word[index] == '_' and word_to_guess[index] == character:
            new_word += character
        else:
            new_word += letter

    return new_word


def check_letter(character, list_to_iterate):
    for letter in list_to_iterate:
        if letter == character:
            return True


def display_wrong_choice(player_guess_letter):
    wrong_letters = ""
    for letter in player_guess_letter:
        wrong_letters += '\u0336'.join(letter) + '\u0336'

    return wrong_letters


def clean_screen():
    system('cls')


if __name__ == '__main__':
    main()

