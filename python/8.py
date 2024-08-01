def offer(c):
    for i in range(n_gods):
        print(f"God {i+1} : ", end="")
        if (c - 7) >= 0:
            print("offered 7")
        else:
            print(f"offered {max(0, c)} needs {7-max(0, c)} more")
        c-=7
    return c

n = int(input("Enter the no.of lemons : "))
n_gods = 3

remaining_lemon = offer(n)

if remaining_lemon == 0:
    print("sufficient")
elif remaining_lemon > 0:
    print(f"surplus : {n - 7*n_gods}")
else:
    print(f"insufficient : {7*n_gods - n}")