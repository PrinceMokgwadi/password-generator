import random, string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for i in range(length))

if __name__ == "__main__":
    print("Your new password is:", generate_password())
