numCases = int(input())
cases = []

for i in range(0,numCases):
    cases.append(list(set(input())))

intersects = cases[0]

for i in range(1,numCases):
    intersects = [x for x in cases[i] if x in intersects]

print(len(intersects))