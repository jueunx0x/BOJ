from collections import deque
n, m = map(int, input().split())  # n, m 입력


graph = [list(map(int, input().split())) for _ in range(m)]

# 이동방향 오른쪽.아래
dx = [0,1]
dy = [1,0]

def bfs():
    visited = [[False] * n for _ in range(m)]
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = True

    while Q:
        x, y = Q.popleft()

        if x == m-1 and y == n-1:
            return True

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                Q.append((nx, ny))
    return False

print("Yes" if bfs() else "No")