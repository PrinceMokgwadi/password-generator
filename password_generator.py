#!/usr/bin/env python3
import random
import string
import sys

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        # Prompt for input; if empty, use default 12
        length_input = input("Enter desired password length (default 12): ").strip()
        length = int(length_input) if length_input else 12
    except ValueError:
        length = 12
        print("Invalid input. Using default length 12.", flush=True)

    password = generate_password(length)
    print("\nYour new password is:", password, flush=True)

    # Save to a file
    try:
        with open("generated_passwords.txt", "a") as f:
            f.write(password + "\n")
        print("Password saved to generated_passwords.txt", flush=True)
    except Exception as e:
        print(f"Could not save password to file: {e}", flush=True)

