# Lesson 4: Math and numbers

print("Let's do some math")

print("5 + 3 =", 5 + 3)
print("10 - 4 =", 10 - 4)
print("6 * 7 =", 6 * 7)
print("20 / 5 =", 20 / 5)
print("9 % 4 =", 9 % 4) # This gives the remainder when 9 is divided by 4

# Leeson 4 step 2: Using my own numbers
a = 13
b = 145

print("a + b =", a + b)
print("a * b =", a * b)

# Lesson 4 - Step 3: Math with variables

# Your numbers
age = 13
lucky_number = 145

# Do some math
double_age = age * 2
half_lucky = lucky_number / 2
sum_total = age + lucky_number

# Show results
print("If I doudbled my age, I'd be", double_age)
print("Half of my lucky number is", half_lucky)
print("Together they add up to", sum_total)

# Lesson 4 - Mini Challenge: Character Stats

# Base stats
health = 100
damage = 25
armor = 10

# Simulate taking a hit
damage_taken = damage - armor
health = health - damage_taken

# Show what happened
print("The enemy attacked!")
print("Damage after armor,", damage_taken)
print("Remaining health,", health)