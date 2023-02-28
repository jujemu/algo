d = {
    0: (1, 0),
    1: (0, 1)
}
for n in range(2, 41):
    zero, one = d[n-1]
    zero += d[n-2][0]
    one += d[n-2][1]
    d[n] = zero, one
    
T = int(input())
for _ in range(T):
    result = 0
    N = int(input())
    print(d[N][0], d[N][1])
        