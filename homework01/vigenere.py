def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    k = 0
    firstBigSymbol = 65
    firstSmallSymbol = 97
    lastSmallSymbol = 122 
    lastBigSymbol = 90
    ciphertext = ""
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= firstBigSymbol and ord(plaintext[i]) <= lastBigSymbol:
            ciphertext += chr((ord(plaintext[i]) + (ord(keyword[k]) % firstBigSymbol) - firstBigSymbol) % 26 + firstBigSymbol)
            k = (k + 1) % len(keyword)
        elif ord(plaintext[i]) >= firstSmallSymbol and ord(plaintext[i]) <= lastSmallSymbol:
            ciphertext += chr((ord(plaintext[i]) + (ord(keyword[k]) % firstSmallSymbol) - firstSmallSymbol) % 26 + firstSmallSymbol)
            k = (k + 1) % len(keyword)
        else:
            ciphertext += plaintext[i]
            k = (k + 1) % len(keyword)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    k = 0
    plaintext = ""
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= firstBigSymbol and ord(ciphertext[i]) <= lastBigSymbol:
            plaintext += chr((ord(ciphertext[i]) - ((ord(keyword[k]) % firstBigSymbol) % firstBigSymbol) - firstBigSymbol) % 26 + firstBigSymbol)
            k = (k + 1) % len(keyword)
        elif ord(ciphertext[i]) >= firstSmallSymbol and ord(ciphertext[i]) <= lastSmallSymbol:
            plaintext += chr((ord(ciphertext[i]) - (ord(keyword[k]) % firstSmallSymbol) - firstSmallSymbol) % 26 + firstSmallSymbol)
            k = (k + 1) % len(keyword)
        else:
            plaintext += ciphertext[i]
            k = (k + 1) % len(keyword)

    return plaintext
