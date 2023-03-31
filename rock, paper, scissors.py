import random

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    # Prompt user for their choice
    user_choice = input("\nEnter your choice (rock, paper, or scissors): ")

    # Generate computer's choice randomly
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Print computer's choice
    print(f"\nComputer chose {computer_choice}.\n")

    # Determine the winner of the game
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time!")

    # Ask user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == 'no':
        break

print("Thanks for playing!")
