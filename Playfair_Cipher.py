def Playfair_Cipher(text, key, mode):
    def generate_matrix(key):
        key = ''.join(dict.fromkeys(key.replace("J", "I").upper()))
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = []

        for char in key:
            if char in alphabet and char not in matrix:
                matrix.append(char)

        for char in alphabet:
            if char not in matrix:
                matrix.append(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def format_text(text):
        text = text.upper().replace("J", "I").replace(" ", "")
        formatted = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else 'X'
            if a == b:
                formatted += a + 'X'
                i += 1
            else:
                formatted += a + b
                i += 2
        if len(formatted) % 2 != 0:
            formatted += 'X'
        return formatted

    def find_pos(matrix, char):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return -1, -1

    result = ""
    matrix = generate_matrix(key)
    text = format_text(text)
    step = 1 if mode == "encode" else -1

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_pos(matrix, a)
        row2, col2 = find_pos(matrix, b)

        if row1 == row2:
            result += matrix[row1][(col1 + step) % 5]
            result += matrix[row2][(col2 + step) % 5]
        elif col1 == col2:
            result += matrix[(row1 + step) % 5][col1]
            result += matrix[(row2 + step) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result
