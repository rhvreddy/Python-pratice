from dulwich.porcelain import print_tag
from transformers import prune_layer

word_list = ["aardvark", "baboon", 'camel']


import random

# Step1 ==> Create a variable called 'Lives' to keep track of the number of lives left.
# Set 'Lives' to equal 6.
lives = 6



chosen_word= random.choice(word_list)
print(chosen_word)



placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"The Letter we guess is: {guess}")


    display = ""



    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
             display += "_"
    print(display)


## Step2 ==> If guess is not a letter in the chosen_word, then reduce 'Lives'by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose"
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")


    if "_" not in display:
        game_over = True
        print("You Win.")


## Step3 ==> print the ASCII art from 'stages'
# that corresponds to the current number of 'lives' the user has remaining.


