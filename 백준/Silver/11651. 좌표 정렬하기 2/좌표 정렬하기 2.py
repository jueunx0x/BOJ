import sys
N=int(input())
arr=[]
for i in range(0,N):
    x,y=map(int,sys.stdin.readline().split())
    arr.append((x,y))

arr.sort(key=lambda arr:(arr[1],arr[0]))#두번째 값을 기준으로 정렬하고, 두번째 값이 같을 경우 첫번째값을 기준으로 정렬 

for i in range(N):
    print(arr[i][0],arr[i][1])#x,y를 한꺼번에 출력