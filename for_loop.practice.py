items = ["crayon", "pencil", "pen", "glue", "eraser", "markers"]
for things in items:
    print(f"The item is: {things}")
# This iterates a list of items  


#numbers = [0, 1, 2, 3, 4, 5]


numbers = range(10)
for number in range(10):
    print(number)
#an easier program for line 7 , counts from o up to 10 but oes not inclue 10

#for i in range(100, 200):
    #print(i)

for i in range(100, 200, 10):
    print(i)    
#counts from 10 to 199 by step of 10

colors = ["re", "blue", "green", "yellow"]     
for color in colors:
    print(color)

numbers = range(1, 9) 
for number in range(1, 9):
    print(number)   

even_numbers = range(10, 20, 2)  
for i in range(10, 20, 2):  
    print(i)  
# for counting simple loops you can use i as the variable. use j for an inner loop, & k for the thir inner loop 

#inner loop example

for i in range(5):
    print(i)

for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}") 


#Looping through strings

first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")



#accessing letters by position

first_name = "Brigham"

fourth_letter = first_name[3]
#python counts from o, so 4th counts 0123 instea of 4
#notice the use of square bracket to call up the letter position
print(fourth_letter)


#iterate through each letter through index numbers

word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    print(index)


#access the letter at the index above using square brackets
word = "book"
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f"index: {index} Letter: {letter}")




#instea of typing the number of letters you can let the computer tell the length of the letters
animal_name = input("What is your pet's name? " )
letter_count = len(animal_name)

print(f"Your pet's name has {letter_count} letters")


#combining len function with the index
word = "book"
number_of_letters = len(word)

for index in range(number_of_letters):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")



#the enumerate function can also access both the index and letters directly
first_name = "Brigham"

for i, letter in enumerate{first_name}:
    print(f"The letter {letter} is at position {i}")