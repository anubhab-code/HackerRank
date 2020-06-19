def add(p1, p2):
    return sum((i or j) for i, j in zip(p1, p2))
N, M = (int(i) for i in input().split())
persons = []
for i in range(N):
    persons.append([int(i) for i in list(input())])
totals = []
for i in range(N-1):
    for j in range(i+1, N):
        totals.append(add(persons[i], persons[j]))
highest=max(totals)
print(highest)
print(totals.count(highest))