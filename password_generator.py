import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        length = 12
        print("Invalid input. Using default length 12.")
    
    password = generate_password(length)
    print("Your new password is:", password)

    # Save to a file
    with open("generated_passwords.txt", "a") as f:
        f.write(password + "\n")
