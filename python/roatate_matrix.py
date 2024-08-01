def read_matrix(r, c):
    matrix = []

    for i in range(r):
        a = []
        for j in range(c):
            val = int(input("Enter the value : "))
            a.append(val)
        matrix.append(a)
    
    return matrix

r = int(input("Enter the no.of rows : "))
c = int(input("Enter the no.of cols : "))

matrix = read_matrix(r, c)

for i in range(0, c):
    for j in range(r-1, -1, -1):
        print(matrix[j][i], end=" ")
    print()