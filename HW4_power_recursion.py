def nk(n, k, m): # 세 숫자 n, k, m이 주어졌을 때 n^k를 m으로 나눈 나머지를 반환하는 함수
    if n == 0: # 종료조건 : n이 0인 경우
        return 0
    elif k == 0:
        return 1
    elif k == 1:
        return n % m

    half = nk(n, k//2, m)

    if k % 2 == 0:
        return (half*half) % m
    else:
        return (half*half*n) % m
    return half

t = int(input())
for _ in range(t):
    n, k, m = map(int, input().split())
    print(nk(n, k, m))