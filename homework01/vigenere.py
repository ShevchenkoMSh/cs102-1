def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    k = 0
    ciphertext = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90:
            ciphertext += chr((ord(plaintext[i]) + (ord(keyword[k]) % 65) - 65) % 26 + 65)
            k = (k + 1) % len(keyword)
        elif ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122:
            ciphertext += chr((ord(plaintext[i]) + (ord(keyword[k]) % 97) - 97) % 26 + 97)
            k = (k + 1) % len(keyword)
        else:
            ciphertext += plaintext[i]
            k = (k + 1) % len(keyword)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    k = 0
    plaintext = ""
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
            plaintext += chr((ord(ciphertext[i]) - ((ord(keyword[k]) % 65) % 65) - 65) % 26 + 65)
            k = (k + 1) % len(keyword)
        elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
            plaintext += chr((ord(ciphertext[i]) - (ord(keyword[k]) % 97) - 97) % 26 + 97)
            k = (k + 1) % len(keyword)
        else:
            plaintext += ciphertext[i]
            k = (k + 1) % len(keyword)

    return plaintext
