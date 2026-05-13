import random

NUMBER_OF_ATTEMPTS = 10 # Maximum number of attempts
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
    "error", "program", "project", "folder", "file"] # List of words for the game


def print_status_now(mask_word, attempts, Final_attempts):
    """Prints the current status - word status and attempt status"""
    print()
    print(f"Secret word status: {"".join(mask_word)}")
    print(f"Status of remaining attempts already made {attempts} out of {Final_attempts} attempts")

def init_attempts():
    """A function that defines the initial number of attempts"""
    attempts = 0
    return attempts

def random_word_selection():
    """Randomly select a word from a list of words"""
    return random.choice(WORDS)

def underscore_instead_of_a_word(word):
    """Function creates a hidden word using underscores"""
    number_of_letters = len(word)
    underscore_word = []
    for letter in range(number_of_letters):
        underscore_word.append("_")
    return underscore_word

def user_input_a_character():
    """A function that requests a character input from the user."""
    letter = input("enter your letter: ").lower()
    return letter

def check_user_input_for_correctness(letter):
    """Checking the validity of the signal entered by the user"""
    if letter >= "a" and letter <= "z" and len(letter) == 1 and letter.isalpha():
        return True
    else:
        return False

def check_has_the_letter_already_been_typed(letter, letter_list):
    """Checking whether the signal has already been entered before"""
    if letter not in letter_list:
        letter_list.append(letter)
        return True
    else:
        return False

def update_of_the_hidden_word_by_letter(the_word, the_hidden_word, letter):
    """Updating the hidden word with the typed letter"""
    if letter in the_word:
        for item in range(len(the_word)):
            if the_word[item] == letter:
                the_hidden_word[item] = letter
        return True
    return False

def decrement_the_counter_in_case_of_a_non_existent_character(attempts):
    """Adding 1 to the counter of failed attempts"""
    attempts += 1
    return attempts

def print_game_over(the_hidden_word, the_word):
    """The printouts at the end of the game for the winner and loser"""
    print()
    if "_" not in the_hidden_word:
        print(f"you won! The word is '{the_word}'")
    else:
        print("game over!")

def main():
    """A function that manages the game in order"""
    the_word = random_word_selection() # Choosing the random word
    attempts = init_attempts() # Setting the initial number of attempts to 0
    letter_list = [] # Create a list that stores all the letters that have already been entered
    the_hidden_word = underscore_instead_of_a_word(the_word) # Creating the hidden word
    while attempts < NUMBER_OF_ATTEMPTS and "_" in the_hidden_word: # The loop - as long as the entire word is not completed and we have not reached the maximum number of attempts
        print_status_now(the_hidden_word, attempts, NUMBER_OF_ATTEMPTS)
        letter = user_input_a_character() # Request a signal from the user
        checking = check_user_input_for_correctness(letter) # Checks the character's integrity
        if checking == False:
            print("Error try again!")
            continue
        if check_has_the_letter_already_been_typed(letter, letter_list) == True: # Checks whether the entered character has not already been entered
            if update_of_the_hidden_word_by_letter(the_word, the_hidden_word, letter) == True: # Updating the letter in the hidden word
                continue # Back to typing another letter
            else: # If the letter does not exist in the word
                attempts = decrement_the_counter_in_case_of_a_non_existent_character(attempts) # Add 1 to the counter that counts the incorrect attempts.
        else: # If the word has already been typed and is in the list of typed letters
            print("\nThe letter has already been chosen before!")
    print_game_over(the_hidden_word, the_word) # Prints of the end of the game to win and lose

main() # Enabling the executive function