def d_and_c(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        a = d_and_c(arr[:m])
        b = d_and_c(arr[m:])
        i = j = 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        # Method 1 (system level code)
        # while i < len(a):
        #     result.append(a[i])
        #     i += 1
        # while j < len(b):
        #     result.append(b[j])
        #     j += 1

        # Method 2 (easy method with python)
        result.extend(a[i:])
        result.extend(b[j:])

        return result
    else:
        return arr

        
# a = [6, 3, 7, 8, 2, 1]
arr = [int(i) for i in input("Enter the numbers separated by spaces : ").split()]
print(arr)
print(d_and_c(arr))