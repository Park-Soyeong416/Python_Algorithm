from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i) # 초기 상태

while len(myQueue) > 1:
    myQueue.popleft() #맨 위의 카드를 버림
    myQueue.append(myQueue.popleft()) #그다음 위의 카드를 맨 밑의 카드 밑으로 이동시킴

print(myQueue[0])