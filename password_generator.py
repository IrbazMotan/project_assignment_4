import random
import string

# Welcome the user
print("Welcome to the Password Generator!")

# Get inputs from the user
password_length = int(input("How long should your password be? (Minimum 4 characters): "))
use_uppercase = input("Do you want uppercase letters? (yes or no): ").strip().lower() == "yes"
use_numbers = input("Do you want numbers in your password? (yes or no): ").strip().lower() == "yes"
use_symbols = input("Do you want symbols (e.g., @, #, $)? (yes or no): ").strip().lower() == "yes"

# Function to create a password
def create_password(length, include_uppercase, include_numbers, include_symbols):
    # Make sure the password is long enough
    if length < 4:
        print("Password must be at least 4 characters long for security.")
        return None

    # Prepare the list of characters based on user choices
    characters = string.ascii_lowercase  # Start with lowercase letters
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Make sure the user selected at least one character type
    if not characters:
        print("You need to select at least one type of character for your password.")
        return None

    # Create a secure password
    password = ''.join(random.choices(characters, k=length))
    return password

# Generate the password
password = create_password(password_length, use_uppercase, use_numbers, use_symbols)

# Display the password or an error message
if password:
    print(f"\nYour secure password is: {password}")
else:
    print("Failed to generate a password. Please try again with valid inputs.")
