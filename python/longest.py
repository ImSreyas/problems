# for the given sequence of number, return length of the longest increasing subsequence.

# n = int(input("Enter the number of elements: "))
seq = [5, 15, 6, 5, 12, 1]
seq = [1, 2]
seq = [1, 2, 10, 4, 5, 6]
seq = [10, 10, 10]
seq = [1, 10, 9, 8, 7, 6, 11, 4, 5, 6]

# def seq_len(seq):
#     max = 0
#     if len(seq) == 1: 
#         return 1
#     for (index, value) in enumerate(seq):
#         count = 1
#         cur = value
#         for j in seq[index:]:
#             if cur < j:
#                 count +=1
#                 cur = j
#         if count > max :
#             max = count
#             count = 0
#     return max

# sub_seq_len = seq_len(seq)
# print(sub_seq_len)
        
def find_min(arr, val):
    smallest = val
    index = -1
    flag = False
    for (i, item) in enumerate(arr):
        if val < item and item < smallest:
            smallest = item
            index = i
            flag = True
    if not flag: return -1
    return index

def seq_len(seq):
    max = 0
    if len(seq) == 1: 
        return 1
    for (index, value) in enumerate(seq):
        count = 1
        cur = value
        new_index = index

        while new_index < len(seq)-1:
            min_index = find_min(seq[new_index+1:], cur) 
            if min_index == -1 : break;
            new_index = min_index+new_index+1
            cur = seq[new_index]
            count +=1

        if count > max :
            max = count
            count = 0
    return max

sub_seq_len = seq_len(seq)
print(sub_seq_len)