can_ride = False

firstrider_age = int(input("What is the age of the first rider? "))
firstrider_height = float(input("what is the height of the first rider? "))

is_second_rider = input("is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    secondrider_age = int(input("What is the age of the second rider? "))
    secondrider_height =float(input("What is the height of the second rider? "))
    if (secondrider_age >= 12 and firstrider_age >= 12) and (firstrider_height >= 62 and secondrider_height >= 62):
        can_ride = True
    else:
        can_ride = False
else:
    can_ride = False
if can_ride:
    print("Welcome to the ride.Please be safe and have fun")
else:
    print("Sorry, you may not ride.")            
