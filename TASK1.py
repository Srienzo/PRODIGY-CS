def main():
    # Get user input for the message and shift value
    message = input("Please enter the message you wish to encrypt: ")
    shift = int(input("Please enter the shift value: "))

    # Encrypt the message using the Caesar cipher
    encrypted_message = caesar_cipher(message, shift)
    print("Your encrypted message is:", encrypted_message)
    
    # Decrypt the message using the same Caesar cipher function with a negative shift
    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print("The decrypted message is:", decrypted_message)

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet if necessary
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            # Non-alphabetic characters are added without modification
            result.append(char)
    # Join the list into a single string and return
    return ''.join(result)

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
