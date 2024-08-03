n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

longest = 0
count = 1
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
       count +=1 
    else:
        if longest < count:
            longest = count
            count = 1

print("longest is : ", max(longest, count))

# max = 1
# for i in range(n-1):
#     count = 1
#     val = arr[i]
#     for j in range(i+1, n):
#         if val < arr[j]:
#             count += 1
#             val = arr[j]
#         else:
#             break
#     if max < count:
#         max = count

# print("longest : ", max)