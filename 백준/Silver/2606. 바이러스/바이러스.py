import sys
sys.setrecursionlimit(10**6)
computer = int(sys.stdin.readline())
line = int(sys.stdin.readline())

graph = [[] for _ in range(computer+1)]
visited = [False] * (computer+1)

count = 0

for i in range(line):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global count
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

dfs(1)
print(visited.count(True)-1)