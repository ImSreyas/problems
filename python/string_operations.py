string = input("Enter a string : ")
str_arr = [char for char in string]

key = input("Enter a character to check : ")
print(True if key in string else False)

key = input("Enter a character to remove : ")
print(string.replace(key, "", 1))

num_arr = [num for num in "1234567890"]
print("string without alphabet : ", "".join([i for i in str_arr if i in num_arr]))

num_arr = [num for num in "1234567890"]
print("string without numbers : ", "".join([i for i in str_arr if i not in num_arr]))

key = input("Enter a character to remove : ")
print(string.replace(key, ""))

num = int(input("Enter the n character to be removed : "))
print(string[num:])