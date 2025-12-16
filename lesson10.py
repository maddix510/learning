# Lesson 10: Functions

# Step 1 - Your First Function

def say_hello():
    print("Hello!")
    print("Welcome to my Python program.")

say_hello()

# Step 2 - Functions with Information

def greet(name):
    print("Nice to meet you,", name)

greet("Maddix")
greet("Player")

# Step 3 - Game-Style Function

def attack(enemy):
    print("You attack the", enemy)

attack("Psycho")
attack("Skag")

# Step 4 - Mini Challenge

def show_stats(health, level):
    print("Health:", health)
    print("Level:", level)

show_stats(100, 1)