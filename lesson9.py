# Lesson 9: Dictionairies (key Value)

# Step 1 - Creating a Dictionary

player = {
    "name": "Maddix",
    "health": 100,
    "level": 1
}

print(player)

# Step 2 - Getting Values from a Dictionary

print(player["name"])
print(player["health"])
print(player["level"])

# Step 3 - Changing Values

player["health"] = 80
player["level"] = 2

print("Health:", player["health"])
print("Level:", player["level"])

# Step 4 - Adding New Info

player["Weapon"] = "Blaster"

print(player)

# Step 5 - Mini Challenge

enemy = {
    "type": "Psycho",
    "health": 50,
    "damage": 10
}

print("Type:", enemy["type"])

enemy["health"] = 15
enemy["level"] = 3

print(enemy)