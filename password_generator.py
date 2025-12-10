import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    # Prompt *and* force flush (sometimes terminals need it)
    try:
        length_str = input("Enter desired password length (default 12): ").strip() or "12"
        length = int(length_str)
    except ValueError:
        print("\n⚠  Invalid input. Using default length 12.", flush=True)
        length = 12

    print(f"\n🛠  Length set to: {length}")  # DEBUG line

    password = generate_password(length)
    print(f"\n🔐 Your new password is: {password}", flush=True)

    # Optional save
    save = input("\nSave password to generated_passwords.txt? (y/n): ").lower()
    if save == 'y':
        try:
            with open("generated_passwords.txt", "a") as f:
                f.write(password + "\n")
            print("✅ Password saved.", flush=True)
        except Exception as e:
            print(f"❌ Could not save: {e}", flush=True)

