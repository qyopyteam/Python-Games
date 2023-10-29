import random

def hangman():
    words = ["python", "programming", "hangman", "developer", "game"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6

    while True:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(display_word)
        
        if "_" not in display_word:
            print("Congratulations! You guessed the word. :)")
            break
        
        if attempts == 0:
            print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'. :/")
            break
        
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. :c")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left. :c")
        else:
            print("Correct guess!")

hangman()
