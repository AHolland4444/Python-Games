# Guess the Number Game
# Input an integer from the range of 1 through 10.

import random
end = False
lives = 10
comp = random.randint(1,100)
while (lives >= 1):
    user = int(input("Your guess: "))
    lives -= 1

    if (user > comp):
        print("Your number is too high. Try again.")
        print("Remaining tries:", lives)
    elif (user < comp):
        print("Your number is too low. Try again.")
        print("Remaining tries:", lives)
    else:
        lives = 0
        continue

if (comp == user):
    print("The computer's number was",comp,".", "You Win!")
    lives = 0
    end = True
else:
    print("The computer's number was",comp,".", "You Lose!")
    lives = 0
    end = True

if (end == True):
    print("The end.")