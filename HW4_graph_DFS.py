# 재귀
import sys
sys.setrecursionlimit(1000000)

def DFS(v, List, Check): # v에서 DFS 시작
    print(v, end=" ")
    Check[v] = True # v 방문했으므로 표시
    # 현재 정점 v와 연결된 모든 정점에 대해
    # 방문하지 않았다면, 바로 방문 (DFS 함수 재귀 호출)
    for i in List[v]: # v와 연결된 모든 정점 중에
        if Check[i] == False:   # 아직 가지 않은 v가 있다면
            DFS(i, List, Check) # DFS 다시 시작

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    List = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        List[u].append(v)
        List[v].append(u)
    for i in range(N):
        List[i].sort()

    Check = [False]*N   # 방문여부 확인을 위한 리스트
    DFS(0, List, Check) # 0부터 DFS 시작
    print("")