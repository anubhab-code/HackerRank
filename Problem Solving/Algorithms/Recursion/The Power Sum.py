x=int(input())
n=int(input())
a=[]
counter=0


def b(i):
    global a
    global counter
    b = a[:]
    for g in b:
        if(i+g)<x+1:
            a.append(i+g)
            if i+g == x:
                counter+=1
    a.append(i)
    if i == x:
        counter+=1


for i in range(1,x+1):
  if i**n < x+1:
     b(i**n)


print(counter)