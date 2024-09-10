##== Control Flow with if/ else and conditional operators
from lib2to3.btm_utils import tokens

from numpy.core.defchararray import equal

#If-else statement
print("Welcome to the rollercoaster!")
height = (int(input("What is the height in cm?")))
if height >= 120:
    print("He can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

## Comparison Operators
# > ==> Greater than
# < ==> Less than
# >= ==> Greater than or equal to
# <= ==> less than or equal to

## Introducing the Modulo
number_to_check = int(input("What is the number you want to check?"))

if number_to_check % 2 == 0:
    print("even")
else:
    print("odd")


## Nested If statements and elif statements
## The below code with multiple if-else statement
print("Welcome to the rollercoaster!")
height = (int(input("What is the height in cm?")))
if height >= 120:
    print("He can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pau $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

## The below code with elif statement

print("Welcome to the rollercoaster!")
height = (int(input("What is the height in cm?")))
if height >= 120:
    print("He can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age <22:
        print("Pleas pay 15$")
    else:
        print("Please pau $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


##Multiple If statements in Succession
print("Welcome to the rollercoaster!")
height = (int(input("What is the height in cm?")))
bill = 0
if height >= 120:
    print("He can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        #Add $3 to their bill
        bill += 3  ## OR  bill = bill

    print(f"Your final bill is {bill}")


else:
    print("Sorry you have to grow taller before you can ride.")
