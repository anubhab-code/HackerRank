def isFunnyString(string):
    result = 'Funny'
    l = len(string)-1
    for i in range(int(len(string)/2+1)):
        if abs((ord(string[i+1]) - ord(string[i]))) != abs((ord(string[l-i-1]) - ord(string[l-i]))):
            result = 'Not Funny'
            break
    return result

num = int(input())
strings = []
for i in range(num):
    s = input() 
    strings.append(s)

for i in strings:
    print(isFunnyString(i))