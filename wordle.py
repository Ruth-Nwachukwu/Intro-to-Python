print("Welcome to the word guessing game")

secret_word = "mantle"

guess = input("What is your guess?  ")

guess_count = 0


while guess != secret_word:
    print("your guess was not correct")
    hint = ""
    for i, letter in enumerate(secret_word):
        if i < len(guess) and letter.lower() == (guess)[i]:
            #checking for correct letter in the right position
            hint += letter.upper()
        elif letter.lower() in guess:
            hint += letter.lower()    
            #checks if the letter exists in the secret word but not in the appropriate position 
        else:
            hint += "_ "  
            #when the letters are not present in the secret word
    print(f"Your hint is: {hint}")     

    guess_count += 1

    guess = input("What is your guess? ")

print("Congratulations, you guesse it.")
print(f"It took you {guess_count} guesses")
