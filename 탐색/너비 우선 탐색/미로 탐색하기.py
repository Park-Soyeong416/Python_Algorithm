from collections import deque
#상하좌우를 탐색하기 위한 리스트 선언
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j] = int(numbers[j])

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4): #상하좌우 검색
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < N and y < M: #좌표 유효성 검사
                if A[x][y] != 0 and not visited[x][y]: #벽이 아니고 방문한 적이 없다면
                    visited[x][y] = True #방문한 걸로 바꾸고
                    A[x][y] = A[now[0]][now[1]] + 1 #depth를 추가한다
                    queue.append((x, y))

BFS(0, 0)
print(A[N - 1][M - 1])