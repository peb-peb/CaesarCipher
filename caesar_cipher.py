"""
A Python Script to implement Caesar Cipher.
"""

def cipher(input_string: str, shift_key: int) -> str:
    """
    Implementation of Cipher Technique.
        Params: input_string (required), shift_key (required)
        Returns: encrypted_string
    """
    # Initialise str to store the encrypted message
    encrypted_string = ""
    for text in input_string:
        if text == " ":
            # For Blank Space, encrypted as it is
            encrypted_string += text
        elif text.isupper():
            # For Upper Case
            encrypted_string = encrypted_string + chr(
                (ord(text) + shift_key - 65) % 26 + 65
            )
        else:
            # For Lower Case
            encrypted_string = encrypted_string + chr(
                (ord(text) + shift_key - 97) % 26 + 97
            )
    return encrypted_string


def decipher(encrypt_string: str, shift_key: int) -> str:
    """
    Implementation of DeCipher Technique.
        Params: encrypt_string (required), shift_key (required)
        Returns: decrypted_string
    """
    # Initialise str to store the decrypted message
    decrypted_string = ""
    for text in encrypt_string:
        if text == " ":
            # For Blank Space, encrypted as it is
            decrypted_string += text
        elif text.isupper():
            # For Upper Case
            decrypted_string = decrypted_string + chr(
                (ord(text) - shift_key - 65) % 26 + 65
            )
        else:
            # For Lower Case
            decrypted_string = decrypted_string + chr(
                (ord(text) - shift_key - 97) % 26 + 97
            )
    return decrypted_string


if __name__ == "__main__":
    """
    Function Calling
    """
    mode = int(input("1. Encryption\t2. Decryption - "))
    if mode == 1:
        imput_string = input("Enter the text to be encrypted: ")
        shift = int(input("Enter the shift key: "))
        print("Text before Encryption: ", imput_string)
        print("Shift Key: ", shift)
        print("Encrypted text: ", cipher(imput_string, shift))
    elif mode == 2:
        encrypted_string = input("Enter the text to be decrypted: ")
        shift = int(input("Enter the shift key: "))
        print("Text before Decryption: ", encrypted_string)
        print("Shift Key: ", shift)
        print("Decrypted text: ", decipher(encrypted_string, shift))
    else:
        print("Invalid Selction!") 