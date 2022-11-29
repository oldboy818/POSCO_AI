def binary(data, left, right, q): # 정렬된 리스트에서 q의 위치를 반환하는 함수
    if left > right: # 없는 경우의 중간
        return -1
    mid = (left + right) // 2 # 정렬된 리스트의 중앙값

    if data[mid] == q: # 종료조건 : 원하는 값을 찾은 경우
        return mid

    else: # 재귀조건
        if data[mid] > q:
            subproblem = binary(data, left, mid-1, q)
        elif data[mid] < q:
            subproblem = binary(data, mid+1, right, q)
    return subproblem

t = int(input())
for _ in range(t):
    data = list(map(int,input().split()))
    quary = list(map(int, input().split()))
    ans = []

    for q in quary:
        ans.append(binary(data, 0, len(data)-1, q))

    print(*ans)