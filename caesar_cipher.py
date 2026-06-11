def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    print("--- Caesar Cipher CLI Tool ---")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? (Q to quit): ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter E, D, or Q.")
            continue
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Please enter a whole number.")
            continue
        if choice == 'E':
            encrypted_message = caesar_cipher(message, shift, mode='encrypt')
            print(f"\nEncrypted Message: {encrypted_message}\n")
        elif choice == 'D':
            decrypted_message = caesar_cipher(message, shift, mode='decrypt')
            print(f"\nDecrypted Message: {decrypted_message}\n")

if __name__ == "__main__":
    main()
