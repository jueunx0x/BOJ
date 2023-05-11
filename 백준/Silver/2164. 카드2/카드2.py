from collections import deque

n=int(input())
queue = deque([x for x in range(1, n + 1)])

while True:
    if len(queue)==1:
        print(queue[0])
        break
    queue.popleft()
    queue.rotate(-1)