# computer guess game 

# welcome to user in this game computer have to guess the number that user select in between 1-00 

print("Welcome to the Guess the Number Game!")
print("Think of a number between 1 and 100, and I will try to guess it.")
print("After each guess, let me know if my guess is too High (H), too Low (L), or Correct (C).")

# Set the range and initialize variables
low: int = 1
high: int = 100
attempts: int = 0
feedback: str = ""

# Start guessing
while feedback != "C":
    guess: int = (low + high) // 2  # Guess the middle number
    attempts += 1
    print(f"My guess is: {guess}")
    
    feedback: str = input("Is my guess too High (H), too Low (L), or Correct (C)? ").strip().upper()
    
    if feedback == "H":
        high = guess - 1  # Narrow the range
    elif feedback == "L":
        low = guess + 1  # Narrow the range
    elif feedback == "C":
        print("Yay! I guessed your number", guess, "in", attempts, "attempts!")
    else:
        print("Invalid input. Please respond with 'H', 'L', or 'C'.")
