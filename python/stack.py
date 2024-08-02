# implementation or creation of stack using array

max_size = 10
def push():
    if len(stack) < max_size:
        val = int(input("Enter the value : "))
        print("1 element pushed")
        stack.append(val)
        print(stack)

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("1 element popped")
        stack.pop()
        print(stack)

stack = []
while True:
    choice = int(input("\n1. push\n2. pop\n3. exit\nEnter the operation : "))
    match choice:
        case 1:
            push()
        case 2:
            pop()
        case 3:
            print("Exiting the program")
            exit()
        case _ :
            print("Invalid input")

            
        
