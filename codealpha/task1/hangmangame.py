import random

def play_hangman():
    word_list = ["python", "logic", "matrix", "syntax", "code"]
    secret_word = random.choice(word_list)
    
    max_attempts = 6
    incorrect_guesses = 0
    guessed_letters = [] 
    
    print("Welcome to Hangman!")
    print(f"I have picked a word. You have {max_attempts} incorrect guesses allowed.")
    print("---------------------------------------")

    while incorrect_guesses < max_attempts:
        
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Guessed so far: {guessed_letters}")
        print(f"Lives remaining: {max_attempts - incorrect_guesses}")

        if "_" not in display_word:
            print("\n🎉 CONGRATULATIONS! You guessed the word!")
            return 

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry, '{guess}' is NOT in the word.")

    print("\n💀 GAME OVER.")
    print(f"The secret word was: {secret_word}")

play_hangman()