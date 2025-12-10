#!/usr/bin/env python3

import argparse
import random
import string
from datetime import datetime
import os

# ---------------- CORE LOGIC ---------------- #

def generate_password(length, strong):
    chars = string.ascii_letters + string.digits + string.punctuation

    if strong and length >= 4:
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation),
        ]
        password += [random.choice(chars) for _ in range(length - 4)]
        random.shuffle(password)
        return "".join(password)
    else:
        return "".join(random.choice(chars) for _ in range(length))

def score_password(pwd):
    score = 0
    score += min(len(pwd), 10)
    score += bool(any(c.islower() for c in pwd))
    score += bool(any(c.isupper() for c in pwd))
    score += bool(any(c.isdigit() for c in pwd))
    score += bool(any(c in string.punctuation for c in pwd))
    return min(score, 10)

def label(score):
    if score <= 4:
        return "Weak"
    elif score <= 7:
        return "Medium"
    else:
        return "Strong"

# ---------------- REPORTING ---------------- #

def save_html(passwords):
    filename = "passwords_report.html"
    html = """<html><head><style>
    body{font-family:Arial}
    table{border-collapse:collapse;width:80%;margin:auto}
    th,td{border:1px solid #222;padding:8px;text-align:center}
    th{background:#222;color:white}
    .Weak{background:#f44336;color:white}
    .Medium{background:#ff9800;color:white}
    .Strong{background:#4caf50;color:white}
    </style></head><body>
    <h2 style='text-align:center'>Password Audit Report</h2>
    <table>
    <tr><th>#</th><th>Password</th><th>Score</th><th>Strength</th></tr>
    """

    for i, p in enumerate(passwords, 1):
        s = score_password(p)
        html += f"<tr><td>{i}</td><td>{p}</td><td>{s}</td><td class='{label(s)}'>{label(s)}</td></tr>"

    html += "</table></body></html>"
    open(filename, "w").write(html)
    print(f"[+] HTML report saved as {filename}")

# ---------------- MAIN ---------------- #

def main():
    parser = argparse.ArgumentParser(description="PWGEN - Cybersecurity Password Generator")
    parser.add_argument("-n", "--number", type=int, default=5, help="Number of passwords")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("-s", "--strong", action="store_true", help="Enforce strong passwords")
    args = parser.parse_args()

    passwords = [generate_password(args.length, args.strong) for _ in range(args.number)]

    print("\nNo.  Password           Score  Strength")
    print("----------------------------------------")
    for i, p in enumerate(passwords, 1):
        sc = score_password(p)
        print(f"{i:<4} {p:<18} {sc:<6} {label(sc)}")

    save_html(passwords)

if __name__ == "__main__":
    main()
