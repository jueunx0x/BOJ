from collections import deque
def solution(maps):
    answer = 0
    m = len(maps) #행수
    n = len(maps[0]) #열수
    visited = [[False]*n for _ in range(m)]
    
    to_L = 0
    to_E = 0
    
    start_x,start_y,L_x,L_y = 0,0,0,0
    dx = [-1,1,0,0] #상하
    dy = [0,0,-1,1] #좌우
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start_x,start_y = i,j
    
    q = deque([])
    print(start_x,start_y)
    visited[start_x][start_y] = True
    q.append((start_x,start_y,0))
    #S to L
    while q:
        x,y,dist = q.popleft()
        if maps[x][y] == 'L':
            L_x = x
            L_y = y
            to_L += dist
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append((nx,ny,dist+1))
    print(L_x,L_y)
    #L to E
    visited = [[False]*n for _ in range(m)]
    if to_L == 0 :
        return -1
    visited[L_x][L_y] = True
    q = deque([])
    q.append((L_x,L_y,0))
    while q:
        x,y,dist = q.popleft()
        if maps[x][y] == 'E':
            to_E+=dist
            return to_L+to_E
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append((nx,ny,dist+1))
    print(visited)
    return -1