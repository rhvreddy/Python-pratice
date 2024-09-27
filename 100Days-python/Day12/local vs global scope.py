enemies = 1

def increase_enemies():
    enemies = 2  ## this is called as a local scope
    print(f"enemies inside function: {enemies}")


increase_enemies()  ## this is called as a global scope
print(f"enemies outside function: {enemies}")

# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()
print(player_health)