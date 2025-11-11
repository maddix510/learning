# Lesson 6: Elif Statements

mood = input("How are you feeling today? (happy, tired, angry) ")

if mood.lower() == "happy":
    print("That's great! keep smiling")
elif mood.lower() == "tired":
    print("You should get some rest")
elif mood.lower() == "angry":
    print("Take a deep breath --- it'll be okay")
else:
    print("Thats and interesting mood")

game_type = input("What kind of games do like, action, puzzle, or rpg? ")

if game_type.lower() == "action":
    print("Explosions and adventure! Nice choice!")
elif game_type.lower() == "puzzle":
    print("smart brain! I like puzzle games too.")
elif game_type.lower() == "rpg":
    print("RPGs have amazing stories.")
else:
    print("That's a cool genre")