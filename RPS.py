import random

# Define the options type as a tuple of strings
options: tuple[str, str, str] = ("rock", "paper", "scissors")

# Running flag is a boolean
running: bool = True

# Main game loop
while running:

    # Player's choice and computer's choice
    player: str = None
    computer: str = random.choice(options)

    # Get a valid player choice
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    # Print choices
    print("Player: " + player)
    print("Computer: " + computer)

    # Game logic
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    # Ask if the player wants to play again
    play_again: str = input("Play again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("Thanks for playing!")
