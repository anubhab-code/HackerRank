import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

curr_min = -1
curr_index = 0
while curr_index < n - 1:
    look_index = curr_index + 1
    while look_index < n:
        #print(look_index)
        if A[curr_index] == A[look_index]:
            if curr_min == -1:
                curr_min = look_index - curr_index
            else:
                curr_min = min(look_index - curr_index, curr_min)
        look_index += 1
    curr_index += 1
print(curr_min)