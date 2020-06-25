N = int(input())
st = input()
K = int(input())

result = ""
for i in st:
    if 65 <= ord(i) <= 90:
        s = chr( (ord(i) + K - 65) % 26 + 65 )
    elif  97 <= ord(i) <= 122:
        s = chr( (ord(i) + K - 97) % 26 + 97 )
    else:
        s = i
    result += s
    
print(result)