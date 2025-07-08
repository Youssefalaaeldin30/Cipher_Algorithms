def Monoalphabetic_Cipher(text, key, mode):
    result = ""
    standard_alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()

    if mode == "encode":
        translation_table = str.maketrans(standard_alphabet, key)
    else:
        translation_table = str.maketrans(key, standard_alphabet)

    result = text.lower().translate(translation_table)
    return result
