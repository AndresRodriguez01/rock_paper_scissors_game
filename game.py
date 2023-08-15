import random

# Global variables
ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Main program
choices = [ROCK, PAPER, SCISSORS]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
pc_choice = random.randint(0, 2)  # Generate a random index for the computer's choice

# Validate user input
if user_choice not in ('0', '1', '2'):
    print("Invalid input. Please try again.")
else:
    user_choice = int(user_choice)
    print("You chose:")
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[pc_choice])

    # Determine the winner
    if user_choice == pc_choice:
        print("It's a tie!")
    elif (user_choice == 0 and pc_choice == 2) or (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")

