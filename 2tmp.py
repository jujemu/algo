import time
current = time.time()

n, r = map(int, input().split())
arr = []

def permutation(arr):
    if len(arr) >= r:
        # print(*arr, sep=' ')
        return
    
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            permutation(arr)
            arr.pop()

permutation(arr)
print(time.time() - current)