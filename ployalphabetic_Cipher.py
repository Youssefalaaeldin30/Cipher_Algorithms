def Polyalphabetic_Cipher(text, key, mode):
    result = ""
    key = key.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()

    key_index = 0
    for char in text:
        if char in alphabet:
            text_idx = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_idx = alphabet.index(key_char)

            if mode == "encode":
                new_idx = (text_idx + key_idx) % len(alphabet)
            else:  # decode
                new_idx = (text_idx - key_idx) % len(alphabet)

            result += alphabet[new_idx]
            key_index += 1
        else:
            result += char  # Leave characters outside the alphabet unchanged

    return result
