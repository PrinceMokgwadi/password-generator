import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def save_password(password, filename="saved_passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Password saved to {filename}")

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be positive. Using default length 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    new_password = generate_password(length)
    print("Your new password is:", new_password)

    save_choice = input("Do you want to save this password? (y/n): ").strip().lower()
    if save_choice == "y":
        save_password(new_password)

    input("Press Enter to exit...")
