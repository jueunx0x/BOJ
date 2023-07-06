from collections import deque
import sys

t = int(input())
n= []
dq = deque([])
for i in range(t):
    n = sys.stdin.readline().split()
    if n[0] == 'push_front' :
        dq.appendleft(n[1])
    elif n[0] == 'push_back' :
        dq.append(n[1])
    elif n[0] == 'pop_front' :
        if len(dq)>0:
            print(dq.popleft())
        else : print(-1)
    elif n[0] == 'pop_back' :
        if len(dq)>0:
            print(dq.pop())
        else : print(-1)
    elif n[0] == 'size' :
        print(len(dq))
    elif n[0] == 'empty':
        if len(dq) == 0 :
            print(1)
        else : print(0)
    elif n[0] == 'front' :
        if len(dq) > 0 :
            print(dq[0])
        else : print(-1)
    elif n[0] == 'back' :
        if len(dq) > 0 :
            print(dq[-1])
        else : print(-1)