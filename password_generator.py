import random

# Define the character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Keep asking the user for input until valid conditions are met
while True:
    # Get the user's input for the number of letters, symbols, and numbers
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Calculate the total number of characters
    total_characters = nr_letters + nr_symbols + nr_numbers

    # Check if the total exceeds the limit of 16
    if total_characters > 16:
        print(f"Total number of characters exceeds the limit of 16. You selected {total_characters}. Please try again.")
    else:
        break

# Generate the password
password = []

# Add random letters
for _ in range(nr_letters):
    password.append(random.choice(letters))

# Add random symbols
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Add random numbers
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the password to ensure randomness
random.shuffle(password)

# Join the list into a string and print the final password
final_password = ''.join(password)
print(f"Your password is: {final_password}")
