def hanoi(n, start, end, mid): # n개의 원판을 A에서 B를 거쳐 C로 이동하는 방식을 출력하는 함수
    if n == 0: # 종료 조건
        return 0
    if n == 1: # 종료 조건
        return print('{} -> {}'.format(start, end))
    else: # 재귀조건
        hanoi(n-1, start, mid, end)
        print('{} -> {}'.format(start, end))
        hanoi(n-1, mid, end, start)
        
t = int(input())
for _ in range(t):
    n = int(input())
    hanoi(n, 'A', 'C', 'B')