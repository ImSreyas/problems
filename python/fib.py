# mem 

def find_fib(n, dict={}):
    if n in dict:
        return dict[n]
    if n <= 1:
        return n
    dict[n] = find_fib(n-1, dict) + find_fib(n-2, dict)
    return dict[n]

print(find_fib(10))