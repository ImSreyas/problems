matrix = []

r = int(input("Enter the no.of rows : "))
c = int(input("Enter the no.of cols : "))

if r != c:
    print("The matrix should be a square matrix")
    exit()

for i in range(r):
    a = []
    for j in range(c):
        val = int(input("Enter the value : "))
        a.append(val)
    matrix.append(a)

diag = False
sum = 0
prod = 1
double = []
for i in range(r):
    for j in range(c):
        if i < j:
            sum+=matrix[i][j]
            prod*=matrix[i][j]
        elif i > j:
           double.append(matrix[i][j]*2) 
        else:
            if matrix[i][j] != 0:
                diag = True

if diag:
    print("-1")
else:
    print("1")

if sum > 20:
    print(sum)
else:
    print(prod)
    
print(double)
            


        
