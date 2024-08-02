# Get one string as input, input should be combination of open and close braces or brackets check wheather the string is valid or not using stack

string = input("Enter the string: ")

stack = []
for char in string:
    if char in "({[":
        stack.append(char)
    else:
        if len(stack) == 0:
            print("invalid")
            exit()
        opp = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        if stack.pop() != opp[char]:
            print("invalid")
            exit()

if len(stack) == 0:
    print("valid")
else: 
    print("invalid")


# if open bracket, then push
# if closed brace, then pop
# after completion of scanning if the stack is empty then valid, if not, invalid
# when we pop if there is no element in the stack then it is invalid