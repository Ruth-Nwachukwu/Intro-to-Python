#Guess my number game - Core Challenge

#magic_number = int(input("What is the magic number? "))

#guess = int(input("What is your guess? "))

#if guess < 6:
    #print("Higher")
#elif guess > 6:
    #print("Lower")
#else:
    #print("You guessed it")



#Section 2

#magic_number = int(input("What is the magic number? "))

#guess = int(input("What is your guess? "))

#while guess < 18:
    #print("Higher")
    #guess = int(input("What is your guess? ")) 

#while guess > 18: 
    #print("Lower")
    #guess = int(input("What is your guess? "))
    #magic_number = int(input("What is the magic number? "))
#print("You guessed it")

guess = int(input("What is your guess? "))
guess_count = 0

import random
magic_number = random.randint(1, 100)
print(magic_number)

while guess < magic_number:
    print("Higher")
    guess = int(input("What is your guess? "))
magic_number = random.randint(1, 100)  

while guess > magic_number: 
    print("Lower")
    guess = int(input("What is your guess? "))
    #magic_number = int(input("What is the magic number? "))
guess_count = guess_count + 1


print("You guessed it")

