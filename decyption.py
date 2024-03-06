import os
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, cipher):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_file_path = encrypted_file_path[:-len('.encrypted')]
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    os.remove(encrypted_file_path)  # Remove the encrypted file

# Specify the directory containing the encrypted files
encrypted_directory = r'C:\Users\gohji\OneDrive\Documents\Encrpytion and Decryption data project'

key_file_path = "encryption_key.key"  # Replace with the actual path to your key file
with open(key_file_path, "rb") as key_file:
    key = key_file.read()

# Initialize the Fernet cipher with the key
cipher = Fernet(key)

# Decrypt each encrypted file in the directory and its subdirectories
for root, dirs, files in os.walk(encrypted_directory):
    for file in files:
        if file.endswith('.encrypted'):
            encrypted_file_path = os.path.join(root, file)
            decrypt_file(encrypted_file_path, cipher)

print("Decryption completed successfully. Encrypted files removed.")
