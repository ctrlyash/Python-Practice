"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char # keeps spaces, numbers, symbols
    return result


def decrypt(message, key):
    return encrypt(message, -key)


print("Secret message program")
choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().upper()

if choice == "E":
    text = input("Enter your message:\n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        if not 1 <= key <= 25:
            print("Key must be between 1 and 25")
        else:
            encrypted = encrypt(text, key)
            print("Encrypted message:")
            print(encrypted)
    except ValueError:
        print("Invalid key")

elif choice == "D":
    text = input("Enter your encrypted message:\n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        if not 1 <= key <= 25:
            print("Key must be between 1 and 25")
        else:
            decrypted = decrypt(text, key)
            print("Decrypted message:")
            print(decrypted)
    except ValueError:
        print("Invalid key")

else:
    print("Invalid choice")    

# Secret message program
# Do you want to (E)ncrypt or (D)ecrypt a message? E
# Enter your message:
# Yash is learning python.
# Enter a number between 1 and 25: 3
# Encrypted message:
# Bdvk lv ohduqlqj sbwkrq.

# Secret message program
# Do you want to (E)ncrypt or (D)ecrypt a message? D
# Enter your encrypted message:
# Bdvk lv ohduqlqj sbwkrq.
# Enter a number between 1 and 25: 3
# Decrypted message:
# Yash is learning python.       
