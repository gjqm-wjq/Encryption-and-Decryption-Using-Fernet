import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, cipher):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    encrypted_data = cipher.encrypt(plaintext)
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(file_path)  # Remove the original plaintext file

# Specify the directory containing the text files
directory = r'C:\Users\gohji\OneDrive\Documents\Encrpytion and Decryption data project'
# Generate a key
key = Fernet.generate_key()

# Save the key to a file (keep this safe!)
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Load the key from the file
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

# Initialize the Fernet cipher with the key
cipher = Fernet(key)

# Encrypt each text file in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            encrypt_file(file_path, cipher)

print("Encryption completed successfully.")
