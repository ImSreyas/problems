a = [10, 7, 8, 8, 10, 3, 2]
# a = [10, 10, 8, 8, 10, 8, 2]
# a = [10, 8, 2]
# a = []
# a = [0, 0]

print(a)

count=0
i=0
while i < len(a)-count:
    if a[i] in a[i+1:len(a)-count]:
        a = a[:i] + a[i+1:] + [0]
        count+=1
        i-=1
    i+=1

a = a[:len(a)-count]
print(a)