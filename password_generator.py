import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_passwords(passwords, filename="saved_passwords.txt"):
    with open(filename, "a") as file:
        for pwd in passwords:
            file.write(pwd + "\n")
    print(f"{len(passwords)} passwords saved to {filename}")

if __name__ == "__main__":
    try:
        num_passwords = int(input("Enter how many passwords to generate: "))
        if num_passwords <= 0:
            print("Number must be positive. Using 1 password.")
            num_passwords = 1
    except ValueError:
        print("Invalid input. Using 1 password.")
        num_passwords = 1

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be positive. Using default 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    passwords = [generate_password(length) for _ in range(num_passwords)]

    print("\nGenerated passwords:")
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}: {pwd}")

    save_choice = input("\nDo you want to save these passwords? (y/n): ").strip().lower()
    if save_choice == "y":
        save_passwords(passwords)

    input("\nPress Enter to exit...")
