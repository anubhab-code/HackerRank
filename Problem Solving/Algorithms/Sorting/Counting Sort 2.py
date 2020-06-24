d = {}
for i in range(100):
    d[i] = 0
n = input("")
s = input("")
s = s.split(" ")
for i in s:
    if i == "":
        break
    x = int(i)
    d[x] += 1
for i in d:
    while d[i] > 0:
        print(i, end=" ")
        d[i] -= 1
print()