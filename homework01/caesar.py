import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:

    ciphertext = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90:
            ciphertext += chr((ord(plaintext[i]) + shift - 65) % 26 + 65)
        elif ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122:
            ciphertext += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:

    plaintext = ""
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
            plaintext += chr((ord(ciphertext[i]) - shift - 65) % 26 + 65)
        elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
            plaintext += chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
        else:
            plaintext += ciphertext[i]

    return plaintext
