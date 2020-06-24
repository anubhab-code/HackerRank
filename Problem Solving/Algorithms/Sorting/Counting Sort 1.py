input()
count = [0]*100
for n in map(int, input().split()):
    count[n] += 1
print(" ".join(map(str, count)))