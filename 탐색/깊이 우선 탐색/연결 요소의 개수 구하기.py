import sys
sys.setrecursionlimit(10000)
#파이썬은 재귀함수 깊이가 1000으로 제한이 있기 때문에
#이를 풀어주기 위해 setrecursionlimit을 10000으로 잡은 거임
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)