N = int(input().strip())
n= N
w = 'Weird'
nw = 'Not Weird'
if ((n % 2 == 1) or (n % 2 == 0 and (n>=6 and n<=20))):
    print(w)
else:
    print(nw)