num = int(input("How many pepsi's you want : "))
capacity = 20

def take_it(a):
    for i in range(0, min(a, 20)):
        print("Take your pepsi")
    if a > 20: 
        print("out of stock")
    print("Enjoy your drink")

if num <= 0: 
    print("Thank you for approaching")
else:
    take_it(num)

