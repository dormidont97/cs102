def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for num, letter in enumerate(plaintext):
        if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
            shift = ord(keyword[num % len(keyword)])
            shift -= ord('a') if 'z' >= letter >= 'a' else ord('A')
            letter_code = ord(letter) + shift
            if 'a' <= letter <= 'z' and letter_code > ord('z'):
                letter_code -= 26
            elif 'A' <= letter <= 'Z' and letter_code > ord('Z'):
                letter_code -= 26
            ciphertext += chr(letter_code)
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for num, letter in enumerate(ciphertext):
        if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
            shift = ord(keyword[num % len(keyword)])
            shift -= ord('a') if 'z' >= letter >= 'a' else ord('A')
            letter_code = ord(letter) - shift
            if 'a' <= letter <= 'z' and letter_code < ord('a'):
                letter_code += 26
            elif 'A' <= letter <= 'Z' and letter_code < ord('A'):
                letter_code += 26
            plaintext += chr(letter_code)
        else:
            plaintext += letter
return plaintext
