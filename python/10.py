def rotate(s, n):
    if n == 1:
        s = s[1:]+s[0]
    elif n == -1:
        s = s[-1]+s[:-1]
    return s

def check_odd_or_even(n):
    sum=0
    while n>0:
        r = n%10
        sum+=r*r
        n//=10
    return sum%2 == 0

inp = input("Enter the input : ")
string, num = inp.split(":")
string, num = string.strip(), int(num.strip())

is_odd_or_even = check_odd_or_even(num)
rotated_arr = rotate(string, 1) if is_odd_or_even else rotate(string, -1)
print(rotated_arr)