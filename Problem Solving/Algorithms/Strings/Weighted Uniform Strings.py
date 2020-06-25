s,n = input().strip(),int(input().strip())
char,i = s[0],1
arr,_len = set(),len(s)
for j in range(1, _len+1):
    if j < _len and s[j] == char:
        arr.add(i*(ord(char)-96))
        i+=1
    else:
        arr.add(i*(ord(char)-96))
        if j < _len:
            i,char = 1, s[j]
    
for a0 in range(n):
    x = int(input().strip())
    print("Yes" if x in arr else "No")