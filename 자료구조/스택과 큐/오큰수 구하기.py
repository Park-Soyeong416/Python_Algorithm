import sys
N = int(input())
ans = [0] * N
A = list(map(int, input().split()))
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        #스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    #반복문을 다 돌고 나왔는데 스택이 비어 있지 않다면 빌 때까지
    ans[myStack.pop()] = -1

for i in range(N):
    sys.stdout.write(str(ans[i]) + " ")
