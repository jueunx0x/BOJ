from collections import deque
def solution(n, wires):
    answer = -1

    #wire 하나씩 전부 끊어보기. 
    for cut in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        for idx,(a,b) in enumerate(wires):
            if idx == cut:
                continue
            graph[a].append(b)
            graph[b].append(a)
        #bfs
        q = deque([(1)])
        print(graph)
        total = 0
        while q:
            node = q.popleft()
            for next_node in graph[node]:
                print(node, next_node)
                if visited[next_node] == False:
                    visited[next_node] = True
                    total+=1
                    q.append((next_node))
        
        print("total",total)
        if answer == -1 or answer > abs(total - (n - total)):
            answer = abs(total - (n - total))

    return answer