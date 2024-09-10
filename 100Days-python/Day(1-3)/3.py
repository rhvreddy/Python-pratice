##== Treasure Island
from unittest.mock import right

print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n'). lower() ## "\" used as escape symbol in programming

if choice1 == "left":
    # Continue in game
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        # game will continue
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exists. Game Over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fall in to a hole. Game Over.")

