#Practicing math expressions
number = 7
print(f"The number is {number}.")
age = input("How old are you? ")
print(f"On your next birthday, you will be", int(age) + 1)
print()
#another metho can be 
age = int(input("How ol are you? "))
next_year_age = age + 1
print(f"On your next birthay, you will be {next_year_age}.")
egg_count = input("How many egg cartons do you have? ")
print(f"You have", int(egg_count) * 12)
print()
cookie_count =input("How many cookies do you have? ")
people_count = input("How many people are there? ")
print(str("Each person may have"), int(cookie_count) / int(people_count), "cookies")