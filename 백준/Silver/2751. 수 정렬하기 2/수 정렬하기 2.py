import sys
n=int(sys.stdin.readline())#더빠르게 읽을 수 있음!! 시간 초과 시 sys 잊지말자.
num=[]

for i in range(0,n):
    num.append(int(sys.stdin.readline()))

num.sort()
for i in num:
    print(i)