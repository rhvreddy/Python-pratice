import random
letters = ['a', 'b', 'c', 'd', 'e', 'A', 'B', 'C', 'D', 'E']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your passwords?\n"))
nr_numbers = int(input("How many numbers would you like to have?\n"))
nr_symbols = int(input("How many symbols would you like to have?\n"))

# Easy Level
# password = ""
#
# # nr_letters = 4
# for char in range(0, nr_letters ):
#     # 1 -4
#     random_char = random.choice(letters)
#     print(random_char)
#     password += random_char
#     # print(password)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# print(f"Your password is {password}")


## Hard level

password_list = []
for char in range(0, nr_letters):
        password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your Password is: {password}")