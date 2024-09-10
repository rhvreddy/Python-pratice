import random
friends = ["harsha", "manish", "vamsi", "Kiran"]

# 1 Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])