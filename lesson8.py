# Lesson 8: Lists

# Step 1 - Creating List

favorite_games = ["Borderlands 2", "Minecraft", "Pokemon"]
print(favorite_games)

# Step 2 - Accessing Items

print(favorite_games[0]) # first item
print(favorite_games[1]) # second item
print(favorite_games[2]) # third item

# Step 3 - Adding and removing items

favorite_games.append("Terraria") # Add a game
print(favorite_games)

favorite_games.remove("Minecraft") # Remove a game
print(favorite_games)

# Step 4 - Mini Challenge

favorite_shows = ["Supernatural", "NCIS", "The good place"]
print(favorite_shows[0])

favorite_shows.append("Stranger Things")
favorite_shows.remove("The good place")

print(favorite_shows[2])