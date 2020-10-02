if __name__ == '__main__':
    input()
    arr = list(map(int,input().split()))
    print(max([i for i in arr if x!=max(arr)]))