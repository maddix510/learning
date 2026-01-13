# Lesson 12 - While loops with user control

# Step 1 - The basic idea

running = True

while running:
    print("The program is running.")
    running = False

# Step 2 - User-Controlled Loop

running = True

while running:
    choice = input("Type 'play' or 'quit': ")

    if choice.lower() == "play":
        print("The game is running...")
    elif choice.lower() == "quit":
        print("Goodbye!")
        running = False
    else:
        print("I don't understand that command.")

# Step 3 - Mini Callenge

Running = True

while Running:
    Choice = input("Your health is at 40. Type 'heal' to restore health or 'exit' to quit: ")
    if Choice.lower() == "heal":
        print(" You're health went up to 50, it can not go higher")
    elif Choice.lower() == "exit":
        print("Exiting the game. Goodbye!")
        Running = False
    else:
        print("Invalid command. Please type 'heal' or 'exit'.")
