
def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for letter in plaintext:
        if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
            letter_code = ord(letter) + 3
            if letter_code > ord('Z') and letter_code < ord('a')\
                    or letter_code > ord('z'):
                letter_code -= 26
            ciphertext += chr(letter_code)
        else:
            ciphertext += letter
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for letter in ciphertext:
        if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
            letter_code = ord(letter) - 3
            if letter_code > ord('Z') and letter_code < ord('a')\
                    or letter_code < ord('A'):
                letter_code += 26
            plaintext += chr(letter_code)
        else:
            plaintext += letter

    return plaintext
