import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i)) #데이터, 인덱스 저장

Max = 0
A.sort()

for i in range(N):
    if Max < A[i][1] - i:
        Max = A[i][1] - i #최대로 왼쪽으로 얼마만큼 원소가 이동했는가

print(Max + 1) #1을 더하는 이유는 마지막에 정렬이 다 되었는지
               #루프를 돌면서 확인하기 때문이다