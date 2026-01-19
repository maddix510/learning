# Lesson 13 - Tiny Text Game

# Step 1 - Player Data (Game State)

player = {
    "name": "Maddix",
    "health": 100,
    "level": 1,
}

#Step 2 - A Function to Show Stats

def show_stats(player):
    print("----- PLAYER STATS -----")
    print("Name:", player["name"])
    print("Health:", player["health"])
    print("Level:", player["level"])
    print("------------------------")

# Step 3 - The Game Loop (Core of the Game)

running = True

while running:
    choice = input("Type: stats, play, quit, or heal: ")

    if choice.lower() == "stats":
        show_stats(player)

    elif choice.lower() == "play":
        print("You explore the area...")
        player["health"] = player["health"] - 10
        print("You lost 10 health!")

        if player["health"] <= 0:
            print("Game Over!")
            running = False

    elif choice.lower() == "heal":
        print("You ate a apple")
        player["health"] = player["health"] + 10
        print("You gained 10 health!")

    elif choice.lower() == "quit":
        print("Thanks for playing!")
        running = False
    
    else:
        print("Unknown command.")

# Step 4 - Mini Challenge (Optional)