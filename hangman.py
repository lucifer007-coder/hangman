import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def is_game_over(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    max_attempts = 6

    while True:
        display = display_word(word, guessed_letters)
        print(display)

        if is_game_over(word, guessed_letters):
            print("Congratulations! You guessed the word: {}".format(word))
            break

        if len(guessed_letters) >= max_attempts:
            print("Sorry, you've run out of attempts. The word was: {}".format(word))
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            print("Incorrect guess!")
            print("Attempts left: {}".format(max_attempts - len(guessed_letters)))

if __name__ == "__main__":
    hangman()
