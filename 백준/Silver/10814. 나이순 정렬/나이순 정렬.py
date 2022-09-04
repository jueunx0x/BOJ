import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(0,N):
    x,y=map(str,sys.stdin.readline().split())
    x=int(x)
    arr.append((x,y))

arr.sort(key=lambda arr:arr[0])#나이순으로 정렬


for i in range(N):
    print(arr[i][0],arr[i][1])