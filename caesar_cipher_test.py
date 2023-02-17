import caesar_cipher
import pytest

@pytest.mark.parametrize(
    "input_text,shift,encrypted_text",
    [
        ("Hello World", 13, "Uryyb Jbeyq"),
        ("HELLO WORLD", 2, "JGNNQ YQTNF")
    ]
)
def test_cipher(input_text, shift, encrypted_text):
    assert caesar_cipher.cipher(input_text, shift) == encrypted_text

@pytest.mark.parametrize(
    "encrypted_text,shift,decrypted_text",
    [
        ('Uryyb Jbeyq', 13, 'Hello World'),
        ('JGNNQ YQTNF', 2, 'HELLO WORLD')
    ]
)
def test_decipher(encrypted_text, shift, decrypted_text):
    assert caesar_cipher.decipher(encrypted_text, shift) == decrypted_text