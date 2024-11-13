import random
import string

def generate_password(length=12):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example: generate a password of 12 characters
password = generate_password(12)
print("Generated Password:", password)
