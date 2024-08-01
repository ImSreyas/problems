import random

a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))

r_number = random.randrange(range(a,b))

count = 0
while count < 3: 
    num = int(input("Enter your guess : "))
    count = count + 1
    if num < r_number:
        print("Lower")
    elif num > r_number: 
        print("higher")
    else: 
        print("Total number of guesses is : ", count)
        exit()

if count >= 3:
    print("You have failed")