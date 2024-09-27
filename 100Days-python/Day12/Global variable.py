# Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies insdie function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#################

enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

increase_enemies(enemies)
print(f"enemies outside function: {enemies}")