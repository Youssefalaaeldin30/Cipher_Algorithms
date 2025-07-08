def RailFence_Cipher(text, depth, mode):
    try:
        depth = int(depth)
    except ValueError:
        return "Depth must be a valid number."

    if depth <= 1:
        return text

    if mode == "encode":
        rail = ['' for _ in range(depth)]
        dir_down = False
        row = 0

        for char in text:
            rail[row] += char
            if row == 0 or row == depth - 1:
                dir_down = not dir_down
            row += 1 if dir_down else -1

        return ''.join(rail)

    else:  # decode
        rail = [['\n' for _ in range(len(text))] for _ in range(depth)]
        dir_down = None
        row, col = 0, 0

        for i in range(len(text)):
            if row == 0:
                dir_down = True
            if row == depth - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1

        index = 0
        for i in range(depth):
            for j in range(len(text)):
                if rail[i][j] == '*' and index < len(text):
                    rail[i][j] = text[index]
                    index += 1

        result = ''
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0:
                dir_down = True
            if row == depth - 1:
                dir_down = False
            result += rail[row][col]
            col += 1
            row += 1 if dir_down else -1

        return result
