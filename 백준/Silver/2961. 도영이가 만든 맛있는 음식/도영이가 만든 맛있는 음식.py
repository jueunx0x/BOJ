from itertools import combinations
import math

n = int(input())
S,B = [],[]
taste_diff =[]
taste_s,taste_b = 0,0
for i in range(n):
    s,b = map(int,input().split())
    S.append(s)
    B.append(b)
for i in range(1,n+1):
    #1개씩 했을 때
    taste_diff.append(abs(S[i-1]-B[i-1]))
    #n개씩 했을 떄
    for j,l in zip(list(combinations(S, i)),list(combinations(B, i))):
        taste_s = math.prod(j)
        taste_b =sum(l)
        taste_diff.append(abs(taste_s-taste_b))
    taste_s,taste_b = 0,0
print(min(taste_diff))