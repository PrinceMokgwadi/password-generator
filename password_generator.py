#!/usr/#!/usr/bin/env python3

import sys
import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        # Use input() instead of sys.stdin.readline() for cross‑terminal compatibility
        length_input = input("Enter desired password length (default 12): ").strip()
        length = int(length_input) if length_input else 12
    except ValueError:
        print("\nInvalid input. Using default length 12.", flush=True)
        length = 12

    password = generate_password(length)
    print(f"\nYour new password is: {password}", flush=True)

    # Optional save
    save = input("Save password to generated_passwords.txt? (y/n): ").lower()
    if save == 'y':
        try:
            with open("generated_passwords.txt", "a") as f:
                f.write(password + "\n")
            print("Password saved.", flush=True)
        except Exception as e:
            print(f"Could not save: {e}", flush=True)
