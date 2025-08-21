import sys
from collections import deque


n = int(sys.stdin.readline())               # totalCount
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 최단 거리(촌수) 계산: 없으면 -1
dist = [-1] * (n + 1)
q = deque([a])
dist[a] = 0
while q:
    cur = q.popleft()
    if cur == b:        # b에 도달하면 종료해도 됨
        break
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

print(dist[b])