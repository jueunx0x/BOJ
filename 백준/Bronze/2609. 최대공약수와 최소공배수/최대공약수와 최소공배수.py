import sys
import math
A,B=map(int,sys.stdin.readline().split())
max=0
min=0
max=math.gcd(A,B)
min=int((A*B)/max)
print(max)
print(min)