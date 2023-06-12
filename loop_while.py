number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry you have entere a negative number")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")