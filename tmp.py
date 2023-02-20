from collections import deque
N, K = map(int, input().split())

def bfs():
    cnt = 0
    q = deque([(N, cnt)])
    
    while q:
        nN, cnt = q.popleft()
        
        l, r, t = nN-1, nN+1, nN*2
        if K in [l,r,t]:
            return cnt+1
        
        if l >= 0:
            q.append((l, cnt+1))
        if r <= 100000:
            q.append((r, cnt+1))
        if t <= 100000:
            q.append((t, cnt+1))
    return cnt
print(bfs() if N != K else 0)
