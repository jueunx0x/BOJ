import sys
from collections import deque

# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)
# 세로길이 N(1 ≤ N ≤ 50)
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)


def bfs(x, y):
    global count
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True
    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                Q.append((nx,ny))


T = int(sys.stdin.readline())

#위,아래,왼쪽,오른쪽
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count_arr = []
for i in range(T):
    count = 0
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    for k in range(M):
        for l in range(N):
            if not visited[k][l] and graph[k][l] == 1:
                count += 1
                bfs(k,l)

    count_arr.append(count)


for i in count_arr:
    print(i)

