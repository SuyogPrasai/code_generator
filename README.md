# Encryption and Decryption Script 🔐📜

Welcome to the Encryption and Decryption Script! This Python script provides a simple yet effective way to encrypt and decrypt text using a custom encryption key. This script can be used to secure sensitive information or communicate securely.

## How It Works 🛠️

The script employs a custom encryption key, stored in a JSON file (`data/encryption_key.json`), which maps characters from the input text to their corresponding encrypted values. The encryption process is based on character types, including capital letters, small letters, numbers, and special characters.

## Features ✨

- **Encryption**: Securely encrypt your text using the provided encryption key.
- **Decryption**: Decrypt previously encrypted text to recover the original content.
- **Customizable**: You can customize the encryption key in the `data/encryption_key.json` file.
- **Easy-to-Use**: The script is easy to integrate into your projects and applications.

## Usage 🚀

To use this Encryption and Decryption Script, follow these steps:

1. Ensure that you have the necessary Python environment set up.

2. Open the script and customize the `data/encryption_key.json` file to define your encryption key. Modify the mapping of characters as needed.

3. Initialize the `generator` class in your Python code:

   ```python
   my_encryptor = generator()
    ```

4. Encrypt your text:

     ```python 
    encrypted_text = my_encryptor.encrypt("Your text to be encrypted.")
    ```

5. Decrypt the text, if needed:
    ```python
    decrypted_text = my_encryptor.decrypt(encrypted_text)
    ```

6. Use the encrypted_text or decrypted_text in your application as required.

## Customization 🛠️
You can customize the encryption key by modifying the data/encryption_key.json file. This file defines how characters are mapped to their encrypted counterparts. Be cautious when making changes to ensure consistency in encryption and decryption.

## License 📝
This script is provided under the MIT License - see the LICENSE file for details.

## Contact 📧
If you have any questions or need assistance with using this Encryption and Decryption Script, please feel free to contact the me at suyog224356@gmail.com.

Thank you for using the Encryption and Decryption Script! Enjoy secure data handling and communication. 🚀🔐📜
