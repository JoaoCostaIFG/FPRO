def mult(M, N):
    lines = len(M)
    cols = len(N[0])
    aux_index = len(M[0])
    result = [[0 for i in range(cols)] for j in range(lines)]
    for i in range(lines):
        for j in range(cols):
            for k in range(aux_index):
                result[i][j] += M[i][k] * N[k][j]
    return result
