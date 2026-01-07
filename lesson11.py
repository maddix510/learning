# Lesson 11: Return Values

# Step 1 - A very simple return

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)

# Step 2 - Why this is powerful

total = add_numbers(10, 20)
double_total = total * 2

print("Total:", total)
print("Double total:", double_total)

# Step 3 - Game-Style Example

def calculate_damage(attack, armor):
    damage = attack - armor
    if damage < 0:
        damage = 0
    return damage

hit = calculate_damage(25, 10)
print("Damage dealt:", hit)

# Step 4 - Mini Challenge

def level_up(level):
    new_level = level + 1
    return new_level

current_level = level_up(5)
print("Your new level is:", current_level)

# Step 5 - Functions + Return + Dictionaries

player = {
    "level": 5
}

def level_up(player):
    player["level"] = player["level"] + 1
    return player["level"]

new_level = level_up(player)
print("Your new level is", new_level)