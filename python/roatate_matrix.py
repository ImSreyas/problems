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

# clock wise rotation 
# for i in range(0, c):
#     for j in range(r-1, -1, -1):
#         print(matrix[j][i], end=" ")
#     print()

# anti-clock wise rotation 
# for i in range(c-1, -1, -1):
#     for j in range(r):
#         print(matrix[j][i], end=" ")
#     print()

# 180 deg rotation
# for i in range(r-1, -1, -1):
#     for j in range(c):
#         print(matrix[i][j])
        

