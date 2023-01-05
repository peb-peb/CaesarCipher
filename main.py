from caesar_cipher import caesar_encrypt, caesar_decrypt

def main():
    message = input("Enter the message: ")
    encrypted_message = caesar_encrypt(message=message, shift=1)
    print(encrypted_message)
    decrypted_message = caesar_decrypt(message=message, shift=1)
    print(decrypted_message)

if __name__ == "__main__":
    main()