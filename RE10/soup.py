def soup(matrix, word):
    def percorre(m, n, word2):
        if word2 == "":
            return True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if abs(i - m) <= 1 and abs(j - n) <= 1 and matrix[i][j] == word2[0]:
                    if percorre(i, j, word2[1:]):
                        return True
        return False

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == word[0]:
                if percorre(i, j, word[1:]):
                    return chr(i + 65) + str(j + 1)
    return "not found"
