import random
from operator import index

NUMBER_OF_ATTEMPTS = 10
WORDS = [
    "apple", "banana", "orange", "grape", "melon",
    "water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper",
    "computer", "keyboard", "mouse", "screen", "phone",
    "music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest",
    "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "sheep", "goat", "camel",
    "bird", "eagle", "snake", "fish", "shark",
    "pizza", "bread", "cheese", "salad", "soup",
    "coffee", "sugar", "honey", "butter", "cookie",
    "happy", "angry", "funny", "quiet", "brave",
    "smart", "strong", "clean", "dirty", "small",
    "large", "short", "long", "early", "late",
    "green", "yellow", "purple", "black", "white",
    "silver", "gold", "brown", "pink", "blue",
    "summer", "winter", "spring", "autumn", "season",
    "morning", "night", "today", "tomorrow", "yesterday",
    "family", "father", "mother", "brother", "sister",
    "friend", "people", "child", "baby", "woman",
    "man", "doctor", "driver", "soldier", "police",
    "engineer", "artist", "farmer", "chef", "pilot",
    "city", "village", "street", "bridge", "garden",
    "market", "store", "hotel", "airport", "station",
    "travel", "ticket", "train", "plane", "bottle",
    "camera", "picture", "letter", "number", "answer",
    "question", "game", "winner", "player", "score",
    "level", "start", "finish", "secret", "danger",
    "dream", "story", "movie", "book", "lesson",
    "language", "english", "hebrew", "word", "sentence",
    "voice", "sound", "light", "shadow", "fire",
    "earth", "stone", "metal", "wood", "glass",
    "cloud", "rain", "storm", "snow", "wind",
    "heart", "brain", "hand", "finger", "shoulder",
    "body", "face", "mouth", "tooth", "eye",
    "jump", "run", "walk", "swim", "drive",
    "write", "read", "speak", "listen", "learn",
    "build", "break", "open", "close", "catch",
    "throw", "bring", "carry", "choose", "change",
    "create", "delete", "search", "print", "input",
    "output", "random", "python", "function", "variable",
    "loop", "condition", "string", "list", "index",
    "error", "program", "project", "folder", "file"]


def print_status_now(mask_word, attempts, Final_attempts):
    print()
    print(f"Secret word status: {"".join(mask_word)}")
    print(f"Status of remaining attempts already made {attempts} out of {Final_attempts} attempts")

def init_attempts():
    attempts = 0
    return attempts

def random_word_selection():
    return random.choice(WORDS)

def underscore_instead_of_a_word(word):
    number_of_letters = len(word)
    underscore_word = []
    for letter in range(number_of_letters):
        underscore_word.append("_")
    return underscore_word

def user_input_a_character():
    letter = input("enter your letter: ").lower()
    return letter

def check_user_input_for_correctness(letter):
    if letter > "a" and letter < "z":
        return letter

def check_has_the_letter_already_been_typed(letter):
    letter_list = []
    if letter not in letter_list:
        letter_list.append(letter)
        return True

def check_if_the_character_matches_the_word(the_word, the_hidden_word, letter):
    if letter not in the_hidden_word:
        return letter

def update_of_the_hidden_word_by_letter(the_word, the_hidden_word, letter):
    for item in range(len(the_word)):
        if the_word[item] == letter:
            the_hidden_word[item] = letter
    return the_hidden_word

def decrement_the_counter_in_case_of_a_non_existent_character(attempts):
    attempts += 1
    return attempts

def print_game_over(the_hidden_word, the_word):
    print()
    if "_" not in the_hidden_word:
        print(f"you won! The word is '{the_word}'")
    else:
        print("game over!")

def main():
    the_word = random_word_selection()
    attempts = init_attempts()
    the_hidden_word = underscore_instead_of_a_word(the_word)
    while attempts <= NUMBER_OF_ATTEMPTS and "_" in the_hidden_word:
        print_status_now(the_hidden_word, attempts, NUMBER_OF_ATTEMPTS)
        letter = user_input_a_character()
        check_user_input_for_correctness(letter)
        if check_has_the_letter_already_been_typed(letter) == True:
            update_of_the_hidden_word_by_letter(the_word, the_hidden_word, letter)
            update_of_the_hidden_word_by_letter(the_word, the_hidden_word, letter)
            continue
        decrement_the_counter_in_case_of_a_non_existent_character()
    print_game_over(the_hidden_word, the_word)

main()