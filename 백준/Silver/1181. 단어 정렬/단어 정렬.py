import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(0,N):
    x=str(sys.stdin.readline())
    arr.append(x)

arr=list(set(arr))
arr.sort()#알파벳으로 정렬

arr.sort(key=len)#길이를 기준으로 정렬

for i in arr:
    print(i,end='')