N, K = map(int, input().split())
check = [True] * 100001

def bfs():
    cnt = 0
    q = [N]
    check[N] = False
    
    while True:
        tmp = []
        for nN in q:
            l, r, t = nN-1, nN+1, nN*2
            if K in [l,r,t]:
                return cnt+1
            
            if l >= 0 and check[l]:
                check[l] = False
                tmp.append(l)
            if r <= 100000 and check[r]:
                check[r] = False
                tmp.append(r)
            if t <= 100000 and check[t]:
                check[t] = False
                tmp.append(t)
        q = tmp
        cnt += 1
        
print(bfs() if N != K else 0)
