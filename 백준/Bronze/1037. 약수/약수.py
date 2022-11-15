import sys

from typing import List

count=sys.stdin.readline()
factor = list(map(int, sys.stdin.readline().split()))
factor = list(map(int,factor))
factor.sort()
print(factor[0]*factor[len(factor)-1])