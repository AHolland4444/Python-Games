

# Guess the Number Game
# Input an integer from the range of 1 through 100.

while True:
    print("""
Guess the number!
It's a number between 1 through 100.
You have 10 tries.
Go!
""")

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
        print("Congratulations!")
    else:
        print("The computer's number was",comp,".", "You Lose!")
        lives = 0
        print("Game over.")

    reboot = input("Play again? (Y/N): ")
    if (reboot == "N") or (reboot == "n"):
        break
    else:
        continue
