import sys
import math
N=int(sys.stdin.readline())
for i in range(0,N):
    A,B=map(int,sys.stdin.readline().split())
    print(int((A*B)/math.gcd(A,B)))
