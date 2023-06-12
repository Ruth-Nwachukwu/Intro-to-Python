
grade_percent = int(input("What is your grade percent? "))

#testing separate print statement at each grade letter 
#if grade_percent >= 90:
    #letter_grade = "A"
    #print(letter_grade)    
#elif grade_percent >= 80:
    #letter_grade = "B"
    #print(letter_grade)
#elif grade_percent >= 70:
    #letter_grade = "C"
    #print(letter_grade)
#elif grade_percent >= 60:
    #letter_grade = "D"
    #print(letter_grade)
#else:
    #letter_grade= "F"
    #print(letter_grade)

#single print statement and including a congratulatory/encouragement message to the user.
if grade_percent >= 90:
    letter_grade = "A"   
elif grade_percent >= 80:
    letter_grade = "B"
elif grade_percent >= 70:
    letter_grade = "C"
elif grade_percent >= 60:
    letter_grade = "D"
else: 
    letter_grade= "F"
    print()
    print(f"Your letter grade for this course is {letter_grade}")

if grade_percent >= 70:
    print("Congratulations, You passed!")

else:
    print("Don't give up! You can do better next time")

#stretch challenge
if grade_percent >= 90:
    letter_grade = "A"   
elif grade_percent >= 80:
    letter_grade = "B"
elif grade_percent >= 70:
    letter_grade = "C"
elif grade_percent >= 60:
    letter_grade = "D"
else: 
    letter_grade= "F"

grade_sign = ""
last_digit = grade_percent % 10
if last_digit >= 7:
    grade_sign = "+"
elif last_digit <= 3:
    grade_sign = "-"
else:
    grade_sign = ""

print()
print(f"Your letter grade for this course is {letter_grade}{grade_sign}")

#a way to show that grade A and F have no sign
if grade_percent >= 93:
    grade_sign = ""
print(f"Your letter grade for this course is {letter_grade}{grade_sign}")

if grade_percent < 60:
    grade_sign = ""
print(f"Your letter grade for this course is {letter_grade}{grade_sign}")






