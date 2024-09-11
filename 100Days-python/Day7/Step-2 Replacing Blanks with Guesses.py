from dulwich.porcelain import print_tag

word_list = ["aardvark", "baboon", 'camel']


import random
chosen_word= random.choice(word_list)
print(chosen_word)


## Step1 ==> Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)



guess = input("Guess a letter: ").lower()
print(f"The Letter we guess is: {guess}")

## Step2 ==> Crete a "display" that puts the guess letter in the right positions and in the rest of the string

display = ""


for letter in chosen_word:
    if letter == guess:
       display += letter
    else:
        display += "_"
print(display)