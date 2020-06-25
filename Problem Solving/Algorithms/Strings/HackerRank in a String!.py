str = 'hackerrank'

t = int(input())

for i in range(t):
    test = input()
    count = 0
    for j in test:
        if(count < len(str)):
            if j == str[count]:
                count+=1
    if count == len(str):
        print('YES')
    else:
        print('NO')