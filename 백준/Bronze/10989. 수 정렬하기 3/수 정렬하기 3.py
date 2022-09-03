import sys
n=int(sys.stdin.readline())#더빠르게 읽기가능
num=[0]*10001#입력값이 10000까지 이루어질 수 있으니, 10000까지의 리스트를 미리 만들어놓음.

for i in range(0,n):
    num[int(sys.stdin.readline())]+=1
for i in range(10001):
    if num[i]!=0:
        for j in range(num[i]):
            print(i)