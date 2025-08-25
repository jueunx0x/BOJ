import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
painting = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = 0
max_painting = []
#위,아래,왼쪽,오른쪽
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    global count
    painting_extend = 1
    Q = deque()
    Q.append((x,y))
    visited[x][y] = True

    while Q:
        x,y = Q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if painting[nx][ny] == 1:
                    painting_extend+=1
                    Q.append((nx, ny))

    count += 1
    max_painting.append(painting_extend)

#전체탐색 --> gpt 참고
for i in range(n):
    for j in range(m):
        if painting[i][j] == 1 and not visited[i][j]:
            bfs(i,j)
print(count)
print(max(max_painting) if max_painting else 0)