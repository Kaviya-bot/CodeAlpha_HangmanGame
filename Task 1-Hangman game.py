words = ["apple", "berry", "redbanana", "jackfruit", "plum"]

while True:
    try:
        choose_word = int(
            input(
                f"There are {len(words)} words, But enter the letters between[0-4] "
                "Which word would you like to guess? "
            )
        )
        if 0 <= choose_word < len(words):
            break
        else:
            print("Number out of range, try again.")
    except ValueError:
        print("Please enter a whole number.")

guess_word = words[choose_word]
guessed = []                
wrong = 0
max_wrong = 6
hidden = ["_"] * len(guess_word)

print("\nWELCOME TO FRUIT BASED HANGMAN GAME !")
print("Guess the word:", " ".join(hidden))

print(f"The first letter is '{guess_word[0]}'")

while wrong < max_wrong and "_" in hidden:
    letter = input("Guess a letter: ").lower()

    if not letter.isalpha() or len(letter) != 1:
        print("Enter a single alphabetic character.")
        continue
    if letter in guessed:
        print("You've already entered this letter.")
        continue

    guessed.append(letter)

    if letter in guess_word:
        print("Correct!")
        for i, ch in enumerate(guess_word):
            if ch == letter:
                hidden[i] = letter
    else:
        wrong += 1
        print(f"Wrong! You have {max_wrong - wrong} guesses left.")

    print("Word:", " ".join(hidden))
    print("Guessed letters:", ", ".join(sorted(guessed)), "\n")

if "_" not in hidden:
    print(f" Congrats! You won. The word is '{guess_word}'.")
else:
    print(f" OOPS! You lost. The word was '{guess_word}'.")

