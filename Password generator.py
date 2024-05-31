import random
import string

def generate_password(length):
    # Define character sets for the password
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters like !, @, #

    # Ensure the password contains at least one of each type
    if length < 4:
        raise ValueError("Password length must be at least 4 to include letters, digits, and symbols.")

    # Combine all the character sets
    all_characters = letters + digits + symbols

    # Generate password ensuring each character set is represented at least once
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random choices from all character sets
    password += random.choices(all_characters, k=length-3)

    # Shuffle the resulting list to ensure randomness
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

# Prompt the user for the desired password length
try:
    user_length = int(input("Enter the desired length of the password: "))
    generated_password = generate_password(user_length)
    print(f"Generated password: {generated_password}")
except ValueError as e:
    print(f"Error: {e}")