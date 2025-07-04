from collections import deque
N, L = map(int, input().split())
mydeque = deque() #덱 생성
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: #뒤에서부터 값을 비교
        mydeque.pop() #값이 최근 것보다 크면 pop
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i - L: #윈도우 크기를 벗어나면
        mydeque.popleft() #pop
    print(mydeque[0][0], end=' ')