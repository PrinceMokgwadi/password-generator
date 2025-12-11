import argparse
import random
import string
import os
from datetime import datetime
import csv

# -------------------------
# Password generation
# -------------------------
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

# -------------------------
# Scoring passwords
# -------------------------
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

# -------------------------
# Main CLI
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="Advanced Password Generator")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of passwords to generate")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("-c", "--chars", type=str, choices=["letters","digits","symbols","all"], default="all", help="Character set")
    parser.add_argument("-s", "--strong", action="store_true", help="Force at least 1 upper, 1 lower, 1 digit, 1 symbol")
    parser.add_argument("-o", "--output", type=str, help="Output HTML report path")
    parser.add_argument("--csv", type=str, help="Output CSV report path")
    args = parser.parse_args()

    passwords = []
    for _ in range(args.number):
        pwd = generate_password(length=args.length, chars=args.chars, strong=args.strong)
        score = password_score(pwd)
        strength = strength_label(score)
        passwords.append((pwd, score, strength))

    # Display table
    print("\nNo.   Password             Score  Strength")
    print("-"*40)
    for i, (pwd, score, strength) in enumerate(passwords, 1):
        print(f"{i:<5} {pwd:<18} {score:<6} {strength}")

    # Prepare HTML
    html_content = "<html><head><title>Password Report</title></head><body>"
    html_content += "<h2>Password Report</h2><table border='1'><tr><th>No.</th><th>Password</th><th>Score</th><th>Strength</th></tr>"
    for i, (pwd, score, strength) in enumerate(passwords, 1):
        html_content += f"<tr><td>{i}</td><td>{pwd}</td><td>{score}</td><td>{strength}</td></tr>"
    html_content += "</table></body></html>"

    # Save HTML
    if args.output:
        html_path = os.path.abspath(args.output)
        os.makedirs(os.path.dirname(html_path), exist_ok=True)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"\nHTML report saved to {html_path}")

    # Save CSV
    if args.csv:
        csv_path = os.path.abspath(args.csv)
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["No.", "Password", "Score", "Strength"])
            for i, (pwd, score, strength) in enumerate(passwords, 1):
                writer.writerow([i, pwd, score, strength])
        print(f"CSV report saved to {csv_path}")
