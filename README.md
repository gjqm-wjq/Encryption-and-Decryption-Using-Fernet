# Encryption and Decryption Using Fernet

This repository contains Python scripts to encrypt and decrypt files using the Fernet symmetric encryption method from the `cryptography` library.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Encryption](#encryption)
  - [Decryption](#decryption)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Data security is a critical concern in today's digital age. Encrypting sensitive information ensures that even if unauthorized users gain access to the data, they cannot decipher its contents without the decryption key. This project provides a simple solution for encrypting and decrypting files using the Fernet encryption algorithm.

## Requirements

To use the provided encryption and decryption scripts, ensure you have the following installed:

- Python 3.x
- `cryptography` library (install via `pip install cryptography`)

## Usage

### Encryption

1. Generate an encryption key by running the `generate_key.py` script:


This will create an encryption key file named `encryption_key.key` in the current directory. Keep this file secure as it's necessary for encryption and decryption.

2. Place the files you want to encrypt in a directory.

3. Run the encryption script `encryption.py`, providing the directory path containing the files you want to encrypt:


This will encrypt each file in the specified directory and its subdirectories. Encrypted files will have a `.encrypted` extension.

### Decryption

1. Ensure you have the encryption key file (`encryption_key.key`) generated during the encryption process.

2. Place the encrypted files you want to decrypt in a directory.

3. Run the decryption script `decryption.py`, providing the directory path containing the encrypted files:


This will decrypt each encrypted file in the specified directory and its subdirectories, removing the `.encrypted` extension.

## Notes

- Keep the encryption key (`encryption_key.key`) secure. Loss of this key will result in the inability to decrypt the files.
- Ensure you have backups of both the original files and the encrypted files to avoid data loss.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
