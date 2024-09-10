import random

random_number_0_to_1 = random.random() ## random.random used to generate a random floating point number
print(random_number_0_to_1)

random_number_0_to_1 = random.random() * 10 ## And if we multiply by 10 it will ranges in between 0 to 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)