"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)        
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*().,<>" for c in password)

    score = sum([length <= 8, has_upper, has_digit, has_special])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, "a", encoding="utf-8") as f:
        f.write(encoded_line + "\n")

    print("✅ Credential saved")    

def view_credientials():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return
    
    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||") 
            "*" * len(password)
            print(f"{website} | {username} | {password}")

          
def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")   

        choice = input("Enter your choice: ")  

        match choice    :
            case "1": add_credential()   
            case "2": view_credientials()   
            case "3": break   
            case _: print("Invalid choice")

if __name__ == "__main__":
    main()

# 🔒 Credential Manager
# 1. Add credential
# 2. View credentials
# 3. Update password
# 4. Exit
# Enter your choice: 1
# Website: google.com
# Username: yash@google
# Password: Yash@1234
# ✅ Credential saved

# 🔒 Credential Manager
# 1. Add credential
# 2. View credentials
# 3. Update password
# 4. Exit
# Enter your choice: 1
# Website: oracle.com
# Username: yash@oracle 
# Password: oryash@1234
# ✅ Credential saved

# 🔒 Credential Manager
# 1. Add credential
# 2. View credentials
# 3. Update password
# 4. Exit
# Enter your choice: 2
# google.com | yash@google | Yash@1234
# oracle.com | yash@oracle | oryash@1234

# 🔒 Credential Manager
# 1. Add credential
# 2. View credentials
# 3. Update password
# 4. Exit
# Enter your choice: 4    

# vault.txt content:
# Z29vZ2xlLmNvbXx8eWFzaEBnb29nbGV8fFlhc2hAMTIzNA==
# b3JhY2xlLmNvbXx8eWFzaEBvcmFjbGV8fG9yeWFzaEAxMjM0