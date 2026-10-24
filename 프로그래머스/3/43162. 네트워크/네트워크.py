from collections import deque
def solution(n, computers):
    answer = 0
    graph = [False] * n
    now = 0
    q = deque([])
    for start in range(n):
        if graph[start] == False:
            answer+=1
            now = start
            q.append((now))
        while q:
            now = q.popleft()
            for i in range(n):
                if computers[now][i] == 1 and graph[i] == False:
                    graph[i] = True
                    q.append((i))

    return answer