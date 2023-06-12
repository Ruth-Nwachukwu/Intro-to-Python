#Purpose:Formatting numeric data types
student_count = 5
total_score = 82
average_score = float(total_score / student_count)
#the f function is a shorthand notation,simpler format
print(f"The average for Group B'S quiz is {average_score}.")
#the secon approach is common with java an c#
print("The avearge score is {} for now.".format(average_score))
#defining number of decimals -precision
print(f"The average for Group B's quiz is {average_score:.2f}")
#displaying numbers in scientific or exponent notation



