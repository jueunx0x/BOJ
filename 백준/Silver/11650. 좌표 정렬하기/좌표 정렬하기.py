import sys
N=int(input())
arr=[]
for i in range(0,N):
    x,y=map(int,sys.stdin.readline().split())
    arr.append((x,y))

arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])#x,y를 한꺼번에 출력 