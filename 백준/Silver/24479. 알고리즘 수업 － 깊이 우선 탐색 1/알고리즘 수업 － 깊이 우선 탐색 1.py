import sys
sys.setrecursionlimit(10**6)

N,M,R = map(int,sys.stdin.readline().split())
order = [0]*(N+1)
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
#간선에 따라 그래프 값 입력
#인접리스트 사용
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

def dfs(pos):
    global cnt
    visited[pos] = 1
    order[pos] = cnt
    cnt+=1
    for i in graph[pos]:
        if visited[i] == 0:
            dfs(i)
dfs(R)

for i in range(1,N+1):
    print(order[i])