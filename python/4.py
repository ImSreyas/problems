a = [2, 4, 1, 3, 5]
size = 6

sum_n = (size*(size+1))//2

for i in a:
    sum_n-=i

print("missing number is : ", sum_n)