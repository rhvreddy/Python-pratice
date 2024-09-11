from dulwich.porcelain import print_tag

word_list = ["aardvark", "baboon", 'camel']

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
import random
chosen_word= random.choice(word_list)
print(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()
print(f"The Letter we guess is: {guess}")

# Check if the letter the user guesses (guess) is one of the letters in the chosen_word. print "Right" if it is, "Wrong" if it's not.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")