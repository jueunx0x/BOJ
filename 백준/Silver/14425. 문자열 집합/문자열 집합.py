import sys
N,M=map(int,sys.stdin.readline().split())
M_arr=[0]*M
S=[0]*N
count=0
for i in range(N):
    S[i]=str(sys.stdin.readline())
for i in range(M):
    M_arr[i]=str(sys.stdin.readline())

for i in M_arr:
    if i in S:
        count+=1

print(count)