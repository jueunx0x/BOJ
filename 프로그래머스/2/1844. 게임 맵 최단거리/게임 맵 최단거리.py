from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)  # 행 갯수
    m = len(maps[0])  # 열 갯수

    # 위.아래.좌.우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * m for _ in range(n)]
    visited[0][0] = 0

    Q = deque()
    visited[0][0] = True
    Q.append((0, 0))

    while Q:
        x, y = Q.popleft()

        if x == n-1 and y == m-1:
            answer = maps[x][y]
            return answer

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                #거리 누적
                maps[nx][ny] = maps[x][y] + 1
                Q.append((nx, ny))
    print(visited)
    print("maps::", maps)
    answer = -1
    return answer