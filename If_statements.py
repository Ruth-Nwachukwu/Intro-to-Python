first_number = int(input("What's your first number? "))
sec_number = int(input("What's your second number? "))

if first_number > sec_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_number == sec_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if sec_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")    

print()
user_favorite_animal = input("What is your favorite animal? ")

if user_favorite_animal.lower() == "parrot":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite animal.")    