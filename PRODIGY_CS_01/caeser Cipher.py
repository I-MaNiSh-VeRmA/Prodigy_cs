def encrypt(text, shift):
    """Encrypts the given text using the Caesar Cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypts the given text using the Caesar Cipher."""
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    print("-----------------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please choose 1 for Encrypt or 2 for Decrypt.")
        return

    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == '1':
        result = encrypt(text, shift)
        print("Encrypted message:", result)
    else:
        result = decrypt(text, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
