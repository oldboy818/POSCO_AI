t = int(input())
for _ in range(t):
    N, M = map(int, input().split())

    for i in range(N):
        l = [[] for i in range(N)]    

    for i in range(M):
        u, v = map(int, input().split())
        l[u].append(v)
        l[v].append(u)
    
    for i in range(N):
        l[i].sort()
        print(*l[i])