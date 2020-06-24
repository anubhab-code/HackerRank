def insert_sort(A):
	m = len(A)
  
	for x in range(1,m):
		k = A[x]
		j=x
		while(j>0 and A[j-1]>k):
			A[j] = A[j-1]
			j-=1
      
		A[j]=k
        
	return A

i = int(input())
N = [int(c) for c in input().split()]
N = insert_sort(N)


for a in N:
  print(a, end=" ")