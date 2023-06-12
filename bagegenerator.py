#learning to write variables in strings an formatting
from calendar import month_name


print("Please enter the following information:")
print()
first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
ID_number = input("Id number: ")
Hair_color = input("Hair color: ")
Eyes_color = input("Eyes color: ")
Month = input("Month you started training: ")
Training = input("Completed advance training: ")
print()
#This prints out the card
print("The ID card is:")
print("----------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}") 
print(job_title.title())
#take note of the formatting for the name cases variation/title
print(f"ID: {ID_number}")
print()
print(email_address.lower())
print(phone_number)
print("-----------------------------") 
#Note the spacing alignment - 15, 14 such that the next line aligns in tabs
print("\n"f"Hair: {Hair_color:15} Eyes: {Eyes_color}")
print(f"Month: {Month:14} Training: {Training}")
print("------------------------------")