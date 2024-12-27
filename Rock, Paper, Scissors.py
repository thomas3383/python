import random
import os

# make a function to clear the screen
def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

i = 2
# Save askii in variables
rock_askii = """
___,-------
        ____)
       (_____)
       (_____)
       (____)
---,__(___)
"""

paper_ascii = """
___,-------
       ____)____
          ______)
          _______)
         _______)
---,__________)
"""

scissors_askii = """
___,-------
       ____)____
          ______)
       __________)
      (____)
---,__(___)
"""
# Print a welcome message to the user
print("Welcome to Rock, Paper, Scissors game\n")

while i == 2:
    # Confirm the RULES
    confirm = input("If you don't know the game type (help) for rules or press enter to start:\n").lower()
    cls()
    if confirm == "help":
        print("""      
        **********RULES**********

        1)You choose (rock / paper / scissors) and the computer chooses
        2)Rock smashes Scissors -> Rock wins
        3)Scissors cuts Paper -> Scissors wins
        4)Paper covers Rock -> Paper wins
        """)

    # Ask the user about his choice and change it into small letters
    user_choice = input("Please choose (rock / paper / scissors):\n").lower()

    # Check if user choice is not in ["rock", "paper", "scissors"] print invalid choice
    while user_choice not in ["rock", "paper", "scissors"]:
        cls()
        print(f"Invalid choice; {user_choice} is not decleared")
        user_choice = input("Please choose (rock / paper / scissors):\n").lower()
        
        continue

    cls()    
    # Display user choice in askii
    if user_choice == "rock":
        print(f"\nYour choice: {rock_askii}\n")
    elif user_choice == "paper":
        print(f"\nYour choice: {paper_ascii}\n")
    else:
        print(f"\nYour choice: {scissors_askii}\n")

    # Make the computer choose from this list
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display computer choice in askii
    if computer_choice == "rock":
        print(f"\nComputer chooses: {rock_askii}\n")
    elif computer_choice == "paper":
        print(f"\nComputer chooses: {paper_ascii}\n")
    else:
        print(f"\nComputer chooses: {scissors_askii}\n")

    # Determine the tie cause
    if user_choice == computer_choice:
        print("It's a Tie!\n")
        
    # Determine the winner
    elif(
    (user_choice == "rock" and computer_choice == "scissors")
    or
    (user_choice == "paper" and computer_choice == "rock")
    or
    (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"You win -> {user_choice} Beats {computer_choice}\n")

    # Determine the loser
    else:
        print(f"You lose -> {computer_choice} Beats {user_choice}\n")

    # Ask user if he wants to leave or restart
    restart_or_leave = input("If you want to restart press 'C' or press 'Q' to quit:\n").upper()
    cls()
    if restart_or_leave == 'C':
        sure = input("Are you sure you want to restart; Please type (yes / no):\n").lower()
        cls()
        
        if sure == "yes":
           
            print("Game restarted....\n")
           
            continue
        elif sure == "no":
            sure = input("If you want to restart press 'C' or press 'Q' to quit:\n").upper()
            cls()
            
            if sure == 'C':
                print("Game restarted....\n")
                
                continue
            elif sure == 'Q':
                print("Game ended....\n")
                
                break
            else:
                print(f"Invalid choice.{sure} is not decleared; Game ended....\n")
        else:
            print(f"Sorry, {sure} is not decleared\n")
    elif restart_or_leave == 'Q':
        cls()
        sure = input("Are you sure you want to quit; Please type (yes / no):\n").lower()
       
        if sure == "yes":
           
            print("Game ended....\n")
           
            break
        elif sure == "no":
            sure = input("If you want to restart press 'C' or press 'Q' to quit:\n").upper()
            if sure == 'C':
                print("Game restarted....\n")
                
                continue
            elif sure == 'Q':
                print("Game ended....\n")
                
                break
            else:
                print(f"Invalid choice.{sure} is not decleared; Game ended....\n")
                
                break
        else:
            print(f"Sorry, {sure} is not decleared; Game ended....\n")
            
            break
