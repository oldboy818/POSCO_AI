t = int(input())
for _ in range(t):
    N, M = map(int, input().split())

    Matrix = [[0]*N for _ in range(N)]

    for i in range(M):
        u, v, c = map(int, input().split())
        Matrix[u][v] = c

    for i in range(N):
        print(*Matrix[i])