import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  # 무한대 값 (1e9 = 10억)

V, E = map(int, input().split())
K = int(input())  # 시작 노드 번호

# 그래프 초기화
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

# 간선 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # u → v, 가중치 w

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        # 이미 처리된 노드면 무시
        if distance[now] < dist:
            continue
        
        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))

dijkstra(K)

# 출력
for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])
