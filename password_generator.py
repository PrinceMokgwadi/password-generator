import random
import string
import os
from datetime import datetime

def generate_password(length=12, chars="all", strong=False):
    if chars == "letters":
        characters = string.ascii_letters
    elif chars == "digits":
        characters = string.digits
    elif chars == "symbols":
        characters = string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    if strong and chars == "all" and length >= 4:
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        if length > 4:
            password += [random.choice(characters) for _ in range(length - 4)]
        random.shuffle(password)
        return "".join(password)
    else:
        return "".join(random.choice(characters) for _ in range(length))

def password_score(pwd):
    length = len(pwd)
    categories = sum([
        any(c.islower() for c in pwd),
        any(c.isupper() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(c in string.punctuation for c in pwd)
    ])
    score = min(length + categories * 2, 10)
    return score

def strength_label(score):
    if score <= 3:
        return "Weak"
    elif score <= 6:
        return "Medium"
    else:
        return "Strong"

def backup_file(filename):
    if os.path.exists(filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        os.rename(filename, f"{filename.replace('.html','')}_backup_{timestamp}.html")

def save_html_report(passwords, filename="passwords_report.html"):
    backup_file(filename)
    html_content = f"""
    <html>
    <head>
        <title>Password Report</title>
        <style>
            table {{ border-collapse: collapse; width: 80%; margin: 20px auto; }}
            th, td {{ border: 1px solid #333; padding: 8px; text-align: center; }}
            th {{ background-color: #222; color: white; }}
            .Weak {{ background-color: #f44336; color: white; }}
            .Medium {{ background-color: #ff9800; color: white; }}
            .Strong {{ background-color: #4caf50; color: white; }}
        </style>
    </head>
    <body>
        <h2 style="text-align:center;">Password Report</h2>
        <table>
            <tr><th>No.</th><th>Password</th><th>Score</th><th>Strength</th></tr>
    """
    for i, pwd in enumerate(passwords, 1):
        score = password_score(pwd)
        strength = strength_label(score)
        html_content += f"<tr><td>{i}</td><td>{pwd}</td><td>{score}</td><td class='{strength}'>{strength}</td></tr>\n"
    html_content += "</table></body></html>"

    with open(filename, "w") as f:
        f.write(html_content)
    print(f"\nHTML report saved to {filename}")

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
            print("Length must be positive. Using 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using 12.")
        length = 12

    # Character type
    print("\nChoose character set:")
    print("1: Letters only")
    print("2: Digits only")
    print("3: Symbols only")
    print("4: All characters (strong password option)")
    choice = input("Enter choice (1-4): ").strip()
    if choice == "1":
        chars = "letters"
        strong = False
    elif choice == "2":
        chars = "digits"
        strong = False
    elif choice == "3":
        chars = "symbols"
        strong = False
    else:
        chars = "all"
        strong_choice = input("Enforce at least 1 uppercase, 1 lowercase, 1 digit, 1 symbol? (y/n): ").strip().lower()
        strong = strong_choice == "y"

    passwords = [generate_password(length, chars, strong) for _ in range(num_passwords)]

    # Display table in terminal
    print("\n{:<5} {:<20} {:<6} {:<8}".format("No.", "Password", "Score", "Strength"))
    print("-" * 45)
    for i, pwd in enumerate(passwords, 1):
        score = password_score(pwd)
        strength = strength_label(score)
        print("{:<5} {:<20} {:<6} {:<8}".format(i, pwd, score, strength))

    # Save HTML report
    save_html_report(passwords)

    input("\nPress Enter to exit...")
