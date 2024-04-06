

# Andrew Holland
# 3/25/24
# Project 6: Random Password Generator


# Importing random and setting variables
import random
error = False
level1 = "abcdefghijklmnopqrstuvwxyz"
level2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
level3 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

# Printing the openning message to the user
print("""
Welcome to my Random Password Generator!
      
Only input numbers please.

Complexity Level options:
      
1. Simple
2. Moderate
3. Complex
      
      """)

# Recieving user input and creating an empty list
level = int(input("Please select your Complexity Level (1/2/3): "))
length = int(input("Please specify desired password length (a number higher than 8): "))
tempList = []

# Create error message if the password length isn't long enough
if length <= 8:
    error = True
    print("Password length too short. Please choose a number higher than 8.")

# Check for complexity level and add random characters to list based on level
if (level == 1):
    for unit in range(length):
        choice = random.choice(level1)
        tempList.append(choice)
        continue

elif (level == 2):
    for unit in range(length):
        choice = random.choice(level2)
        tempList.append(choice)
        continue

elif (level == 3):
    for unit in range(length):
        choice = random.choice(level3)
        tempList.append(choice)
        continue
# Create error message if complexity level isn't 1, 2, or 3
else:
    error = True
    print("Invalid complexity option. Please choose from the options; 1, 2, or 3.")

# If no error messages, combine the items in the list into a string and print result
if (error == False):
    x = ""
    password = x.join(tempList)
    print("Your random password:",password)