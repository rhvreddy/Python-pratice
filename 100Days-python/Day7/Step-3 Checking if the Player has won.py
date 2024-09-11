from dulwich.porcelain import print_tag

word_list = ["aardvark", "baboon", 'camel']


import random
chosen_word= random.choice(word_list)
print(chosen_word)



placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

## Step1 ==> Use a while loop to let the user guess again.

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"The Letter we guess is: {guess}")


    display = ""

## Step2 ==> Change the for loop so that you keep the previous correct letters in display.


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
             display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win.")