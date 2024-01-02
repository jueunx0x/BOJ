import sys
T = int(input())
for i in range(0,T):
    A,B = map(int,input().split(','))
    print(A+B)
    A,B = 0,0
