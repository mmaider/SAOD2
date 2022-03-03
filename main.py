# красивенький вывод
def print_matrix(m):
    for i in m:
        print(i)
    print("\n")


# генерация поля
def create_matrix(n):
    arr = []
    for i in range(n):
        arr.append([])
        for j in range(n):
            arr[i].append(-1)
    return arr


# агоритм расстановки королев
def try_eightqueens(matrix, start_pos, sum_queens):
    global finalmatrix
    matrixcopy = []
    for i in range(8):
        matrixcopy.append([])
        for j in range(8):
            tmp = matrix[i][j]
            matrixcopy[i].append(tmp)
    for i in range(8):
        try:
            # поиск первого вхождения свободной ячейки
            idqueen = matrixcopy[start_pos].index(-1)
            # горизонталь + вертикаль
            for t in range(8):
                matrixcopy[start_pos][t] = 0
                matrixcopy[t][idqueen] = 0
            # диагональ 1
            for t in range(min(8 - idqueen, 8 - start_pos)):
                matrixcopy[start_pos + t][idqueen + t] = 0
            # диагональ 2
            for t in range(min(idqueen + 1, 8 - start_pos)):
                matrixcopy[start_pos + t][idqueen - t] = 0
            matrixcopy[start_pos][idqueen] = 1
            # проверка на выход
            if sum_queens == 7:
                # вывод первого решения:
                finalmatrix = matrixcopy
                return True
                # вывод всех решений:
                #print_matrix(matrixcopy)

            # спуск на уровень ниже
            result = try_eightqueens(matrixcopy, start_pos + 1, sum_queens + 1)
            if result:
                return True
            else:
                for i in range(8):
                    for j in range(8):
                        tmp = matrix[i][j]
                        matrixcopy[i][j] = tmp
                for t in range(idqueen + 1):
                    matrixcopy[start_pos][t] = 0
        except Exception:
            return False
    return False


matrix = create_matrix(8)
finalmatrix = []
print("Исходная матрица")
print_matrix(matrix)
print("Пример решения задачи о 8 ферзях:")
a = try_eightqueens(matrix, 0, 0)
print_matrix(finalmatrix)
