n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

max = 0
for i in range(n-1):
    count = 1
    for j in range(len(arr[i+1:])):
        if arr[i] < arr[j]:
            count += 1
        else:
            break
    if max < count:
        max = count

print("longest : ", max)