##== Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What is the size you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: {bill}")


##=== Logical Operators
#AND Operators ==> if both the cases are "true" then the output is true. If any on the case is "false" then the condition is false
# OR Operators ==> if both the cases are "false" then the output is false. Rest all cases it will be "true".
# NOT Operators ==> If the condition is "true" then it will show as "false". If the condition is "false" it will show as "true"


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
    elif age >=45 and age <= 55:
        print("Everything is going to be free ride on us!")
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
