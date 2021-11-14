import random
import functions

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Please choose from the given options")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if (functions.player_wins(user_input, computer_pick)):
        print("You won!")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("It's a draw")

    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")