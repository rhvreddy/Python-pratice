##Python primitive data types

# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123456789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

##== Type Error, Type Checking and Type Conversion
len("Hello")

print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))


#Type conversion
print(int("123") + int("456"))

name_of_the_user= input("Enter your name")
lenght_of_name = len(name_of_the_user)
print(type("Number of letters in your name: ")) #str
print(type(lenght_of_name)) #int


###========Mathematical operations in python
print("My age: " + str(12))
print(123 + 456)
print(7 -3)
print(3 * 2)
print(6 / 3)
print(6 // 3)
print(2 ** 2)

# PEMDAS ==>

# ()
# **
# * OR /
# + OR -

print(3 * 3 + 3 / 3 - 3)
print(6 / (1 + 1) * 3 - 3)


##=== Number manipulation and F strings in python
bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))
print(round(bmi))
print(round(bmi, 2))


score = 0
#User scores a point
score += 1
print(score)

#f-strings
print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

