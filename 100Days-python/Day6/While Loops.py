

##  URL ==> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    jump()

(((OR)))


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()


# For
#
# for item in list_of_items:
#     #Do something to each item
#
# for number in range(a, b):
#     print(number)

# While
#
# while something_is_true:
#     # Do something repeatedly


# Infinite Loop
#
# while 5 > 3:
#     #Do this
#     #Then do this
#     #Then do this