import random

user_choise = int(input("What do you want to choose? Type 0 for Rock, 1 for paper, 2 for scissors.\n"))
# 0, 1, 2
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choise >= 3 or user_choise < 0:
    print("You typed an invalid number. You lose!")
elif user_choise == 0 and computer_choice == 2:
    print("You wins!")
elif computer_choice == 0 and user_choise == 2:
    print("You lose!")
elif computer_choice > user_choise:
    print("You lose!")
elif user_choise > computer_choice:
    print("You Won!")
elif computer_choice == user_choise:
    print("It's a draw!")
