import sys
from collections import deque


n = int(sys.stdin.readline())
hometown =[]
graph = list()
for i in range(n):
    x = sys.stdin.readline().strip()
    graph.append(list(x))

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    count = 1 if graph[x][y] == '1' else 0
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == '1':
                visited[nx][ny] = True
                count += 1
                q.append((nx, ny))
    hometown.append(count)

total_count = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == '1':
            bfs(i,j)
            total_count += 1
print(total_count)
for i in sorted(hometown):
    print(i)