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
   # while sum_queens != 8:
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == -1:
                for t in range(8):
                    matrix[i][t] = 0
                    matrix[t][j] = 0
                for t in range(j):
                    matrix[i+t][j-t] = 0
                for t in range(min(8-j, 8-i)):
                    matrix[i+t][j+t] = 0
                matrix[i][j] = 1
                sum_queens += 1
                print_matrix(matrix)
                break
    print(sum_queens)

matrix = create_matrix(8)
print("Исходная матрица")
print_matrix(matrix)
try_eightqueens(matrix, 0, 0)
