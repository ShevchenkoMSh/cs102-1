import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    firstBigSymbol = 65
    firstSmallSymbol = 97
    lastSmallSymbol = 122
    lastBigSymbol = 90
    ciphertext = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= firstBigSymbol and ord(plaintext[i]) <= lastBigSymbol:
            ciphertext += chr((ord(plaintext[i]) + shift - firstBigSymbol) % 26 + firstBigSymbol)
        elif ord(plaintext[i]) >= firstSmallSymbol and ord(plaintext[i]) <= lastSmallSymbol:
            ciphertext += chr(
                (ord(plaintext[i]) + shift - firstSmallSymbol) % 26 + firstSmallSymbol
            )
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:

    plaintext = ""
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= firstBigSymbol and ord(ciphertext[i]) <= lastBigSymbol:
            plaintext += chr((ord(ciphertext[i]) - shift - firstBigSymbol) % 26 + firstBigSymbol)
        elif ord(ciphertext[i]) >= firstSmallSymbol and ord(ciphertext[i]) <= lastSmallSymbol:
            plaintext += chr(
                (ord(ciphertext[i]) - shift - firstSmallSymbol) % 26 + firstSmallSymbol
            )
        else:
            plaintext += ciphertext[i]

    return plaintext
