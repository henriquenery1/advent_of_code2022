#Write a program that can encrypt and decrypt messages using a simple cipher, such as the Caesar cipher.

def caesar_cipher(message, key):
    # Create an empty string to store the encrypted/decrypted message
    encrypted_message = ""

    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Shift the character by the key and add it to the encrypted message
            encrypted_message += chr(ord(char) + key)
        else:
            # Add the non-letter character to the encrypted message without shifting it
            encrypted_message += char

    return encrypted_message

# Encrypt a message
message = "Hello, world!"
key = 3
encrypted_message = caesar_cipher(message, key)
print(encrypted_message)  # Output: Khoor, zruog!

# Decrypt a message
message = "Khoor, zruog!"
key = -3
decrypted_message = caesar_cipher(message, key)
print(decrypted_message)  # Output: Hello, world!
