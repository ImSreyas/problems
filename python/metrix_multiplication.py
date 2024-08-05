def get_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input()))
        matrix.append(row)
    return matrix
    
def matrix_multiplication(matrix1, matrix2, m, n, p, q):
    result = []
    if n == p:
        for i in range(m):
            a = []
            for j in range(q):
                sum = 0
                for k in range(n):
                    sum += matrix1[i][k] * matrix2[k][j]
                a.append(sum)
            result.append(a)
        return result
    return False
    
a = int(input("Matrix 1\nrows : "))
b = int(input("cols : "))
c = int(input("Matrix 2\nrows : "))
d = int(input("cols : "))

matrix1 = [] 
matrix2 = []
print("Enter matrix 1 : ")
matrix1 = get_matrix(a, b)

print("Enter matrix 2 : ")
matrix2 = get_matrix(c, d)

print(matrix_multiplication(matrix1, matrix2, a, b, c, d) or "matrix multiplication not possible")