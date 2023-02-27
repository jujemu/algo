T = int(input())
for _ in range(T):
    R, s = input().split()
    tmp = set(s)
    for ele in tmp:
        s = s.replace(ele, ele*int(R))
    print(s)