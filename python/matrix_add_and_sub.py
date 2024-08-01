matrix1 = []
matrix2 = []

print("matrix 1")
r1 = int(input("Enter the no.of rows : "))
c1 = int(input("Enter the no.of cols : "))


for i in range(r1):
    a = []
    for j in range(c1):
        val = int(input("Enter the value : "))
        a.append(val)
    matrix1.append(a)

print("matrix 2")
r2 = int(input("Enter the no.of rows : "))
c2 = int(input("Enter the no.of cols : "))

for i in range(r2):
    a = []
    for j in range(c2):
        val = int(input("Enter the value : "))
        a.append(val)
    matrix2.append(a)

print("matrix 1 is :")
for row in range(r1):
    for col in range(c1):
        print(matrix1[row][col], end=" ")
    print()

print("matrix 2 is :")
for row in range(r2):
    for col in range(c2):
        print(matrix2[row][col], end=" ")
    print()

if r1 != r2 and c1 != c2:
    print("Matrix addition and subtraction is not possible")
else:
    sum = []
    sub = []

    for i in range(r1):
        a = []
        b = []
        for j in range(c1):
            val = matrix1[i][j] + matrix2[i][j]
            a.append(val)
            val = matrix1[i][j] - matrix2[i][j]
            b.append(val)
        sum.append(a)
        sub.append(b)

    print("sum matrix is :")
    for row in range(r1):
        for col in range(c1):
            print(sum[row][col], end=" ")
        print()

    print("subtracted matrix is :")
    for row in range(r1):
        for col in range(c1):
            print(sub[row][col], end=" ")
        print()
