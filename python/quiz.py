# quiz = {
#     "1": {
#         "question": "",
#         "options": [""],
#         "ans": []
#     }
# }

q1 = '''1. What was the name given to Android 4.3?
a. Jelly Bean
b. Lollipop
c. Nutella
d. Froyo
'''

q2 = '''2. macos is bases on linux?
a. true
b. false
'''

q3 = '''3. how many district are in kerala?
a. 10
b. 16
c. 14
d. 5
'''

ans = {q1: "a", q2: "b", q3: "c"} 

name = input("Enter your name : ")
print(f"Welcome {name} to this quiz")
score = 0

for i in ans:
    print()
    print(i)

    flag = input("Do you want to skip the question? (yes/no) : ")
    if flag == "yes":
        continue
    
    a = input("Enter your answer : ")
    if a == ans[i]:
        score+=1
        print("Wow your answer is correct. you got 1 point")
    else:
        score=max(score-1, 0)
        print("Wow your answer is not correct. you lose 1 point")
    flag = input("Do you want to quit or not? (yes/no) : ")
    if flag == "yes":
        break

print(f"Your score is : {score}")