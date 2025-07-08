def Caesar_Cipher(text, key, alphabet, mode):
    result = ""
    key = int(key)
    alphabet = alphabet.lower()

    for char in text.lower():
        if char in alphabet:
            idx = alphabet.index(char)
            if mode == "encode":
                new_idx = (idx + key) % len(alphabet)
            else:  # decode
                new_idx = (idx - key) % len(alphabet)
            result += alphabet[new_idx]
        else:
            result += char  # Keep characters that are not in the alphabet unchanged

    return result
