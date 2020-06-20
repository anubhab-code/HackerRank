matrix = [list(map(int, input().split(' '))), list(map(int, input().split(' '))), list(map(int, input().split(' ')))]

lowest = 100 

m1 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
m2 = [[2, 7, 6], [9, 5 ,1], [4, 3, 8]]
m3 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
m4 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
m5 = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
m6 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
m7 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
m8 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

matrices = [m1, m2, m3, m4, m5, m6, m7, m8]

for i in range(0,8):
    temp = matrices[i]
    difference = 0
    for y in range(0,3):
        for x in range(0,3):
            difference += abs(matrix[y][x] - temp[y][x])
    if difference < lowest:
        lowest = difference
    if difference == 0:
        break
print(lowest)