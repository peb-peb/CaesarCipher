"""
V1.0 - only allows lowercase alphabets (ASCII = 97-122)
"""

def caesar_encrypt(message: str, shift: int) -> str:
    """
    
    """
    encrypted_message = ""
    for ch in message:
        ch = ch.lower() # remove this if using ASCII 32-126
        if ch.isalpha():
            encrypted_message += chr((ord(ch) + shift - 97) % 26 + 97)
        else:
            encrypted_message += ch
    return encrypted_message

def caesar_decrypt(message: str, shift: int) -> str:
    """
    
    """
    decrypted_message = ""
    for ch in message:
        ch = ch.lower() # remove this if using ASCII 32-126
        if ch.isalpha():
            decrypted_message += chr((ord(ch) - shift - 97) % 26 + 97)
        else:
            decrypted_message += ch
    return decrypted_message