
import random

computer_choice = random.choice(["rock", "paper", "scissors"])
my_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print("Computer chose:", computer_choice)

if my_choice not in ("rock", "paper", "scissors"):
    print("Invalid choice!")
    exit(0)

if my_choice == computer_choice:
    print("It's a draw!")
    exit(0)
    
if (my_choice == "rock" and computer_choice == "scissors") or \
   (my_choice == "scissors" and computer_choice == "paper") or \
   (my_choice == "paper" and computer_choice == "rock"): 
    print("You win!")
    exit(0)

print("Computer wins!")
