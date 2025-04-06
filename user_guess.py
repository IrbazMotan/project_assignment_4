import random

# Welcome the user and explain the game
print("Welcome to the Guess the Number Game!")
print("I am thinking of a number between 1 and 100. Try to guess it!")
print("After each guess, I'll tell you if your guess is too High (H), too Low (L), or Correct (C).")

# Randomly select a number between 1 and 100
correct_number: int = random.randint(1, 100)

# Initialize variables
low: int = 1
high: int = 100
attempts: int = 0
feedback: str = ""

# Start guessing
while feedback != "C":
    guess: int = int(input(f"Guess a number between {low} and {high}: "))
    attempts += 1
    
    # Check the guess and give feedback
    if guess < correct_number:
        print("Your guess is too low!")
        low = guess + 1  # Update the lower bound for the next guess
    elif guess > correct_number:
        print("Your guess is too high!")
        high = guess - 1  # Update the upper bound for the next guess
    elif guess == correct_number:
        print(f"Yay! You guessed the number {correct_number} correctly in {attempts} attempts!")
        feedback = "C"  # Exit the loop once the correct guess is made
    else:
        print("Invalid input. Please guess a number between 1 and 100.")