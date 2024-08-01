# a = [20, 32, 15, 100, 65]
a = [45, 32, 15, 100, 125]
# a = [0, 10, 5]

if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        if i == 0:
            if a[i] > a[i+1]:
                print(a[i])
        elif i > 0 and i < len(a)-1:
            if a[i] > a[i-1] and a[i] > a[i+1]:
                print(a[i])
        elif i == len(a)-1:
            if a[i] > a[i-1]:
                print(a[i])