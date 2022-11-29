def FIB(n): # 피보나치 수열의 n번째 항을 반환하는 함수
    if n == 1: # 종료조건
        return 1
    elif n == 2: # 종료조건
        return 1
    else: # 재귀호출
        return FIB(n-1) + FIB(n-2)

t = int(input())
for _ in range(t):
    n = int(input())
    print(FIB(n))
