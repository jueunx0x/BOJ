import sys
from collections import deque
count=int(sys.stdin.readline())
n_arr = deque([])
for i in range(0,count):
    n = sys.stdin.readline().split()
    if n[0]=="push":
        n_arr.append(n[1])
    elif n[0]=="pop":
        if len(n_arr) == 0:
            print(-1)
        else:print(n_arr.popleft())
    elif n[0]=="front":
        if len(n_arr)>0:
            print(n_arr[0])
        else: print(-1)
    elif n[0]=="back":
        if len(n_arr)>0:
             print(n_arr[-1])
        else: print(-1)
    elif n[0]=="size":
        print(len(n_arr))
    elif n[0]=="empty":
        if len(n_arr) == 0:
            print(1)
        else: print(0)