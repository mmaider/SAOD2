def print_matrix(m):
    for i in m:
        print(i)
    print("\n")


def create_matrix(n):
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(-1)
    return arr


def try_eightqueens(matrix, start_pos, sum_queens):
    matrixcopy = []
    for i in range(8):
        matrixcopy.append([])
        for j in range(8):
            tmp = matrix[i][j]
            matrixcopy[i].append(tmp)
    for i in range(8):
        print(start_pos)
        print_matrix(matrixcopy)
        try:
            idqueen = matrixcopy[start_pos].index(-1)
            for t in range(8):
                matrixcopy[start_pos][t] = 0
                matrixcopy[t][idqueen] = 0
            # диагональ 1, работает
            for t in range(min(8 - idqueen, 8 - start_pos)):
                matrixcopy[start_pos + t][idqueen + t] = 0
            # диагональ 2 (вроде робит???)
            for t in range(min(idqueen+1, 8 - start_pos)):
                matrixcopy[start_pos + t][idqueen - t] = 0
            matrixcopy[start_pos][idqueen] = 1
            if i != 7:
                result = try_eightqueens(matrixcopy, start_pos+1, sum_queens+1)
                if result:
                    return result
                else:
                    matrixcopy = matrix.copy()
                    for t in range(idqueen+1):
                        matrixcopy[start_pos][t] = 0
            else:
                return matrixcopy
        except Exception:
            return False
    return False


matrix = create_matrix(8)
print("Исходная матрица")
print_matrix(matrix)
a = try_eightqueens(matrix, 0, 0)
if a:
    print_matrix(matrix)
