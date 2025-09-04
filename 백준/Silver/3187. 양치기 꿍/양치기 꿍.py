import sys
from collections import deque

# . 빈공간 / # 울타리 / v 늑대 / k 양



R,C = map(int,sys.stdin.readline().split())

#위,아래,왼쪽,오른쪽
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count_arr = []
graph = list()
visited = [[False] * C for _ in range(R)]

total_sheep = 0
total_wolves = 0

#입력값 받아서 울타리.빈공간.양.늑대 graph에 적재
for i in range(R):
    x = sys.stdin.readline().strip()
    graph.append(list(x))


def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    w,s = 0, 0
    visited[x][y] = True
    if graph[x][y] == 'v':
        w = 1
    if graph[x][y] == 'k':
        s = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != '#':
                visited[nx][ny] = True
                # 늑대
                if graph[nx][ny] == 'v':
                    w += 1
                #양
                elif graph[nx][ny] == 'k':
                    s += 1
                # print(graph[nx][ny])
                Q.append((nx, ny))
    # print(s,w)
    if s > w:
        w = 0
    elif s < w or s == w:
        s = 0
    # print("양,늑대 후위연산 후",s, w)
    return s, w


for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph[i][j] != '#':
            sheep, wolves = bfs(i, j)
            # print(sheep, wolves)
            total_sheep += sheep
            total_wolves += wolves


print(total_sheep,total_wolves)
