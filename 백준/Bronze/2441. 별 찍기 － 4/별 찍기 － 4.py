import sys
N=int(sys.stdin.readline())
for i in reversed(range(1,N+1)):
    print(" "*(N-i)+"*"*i)