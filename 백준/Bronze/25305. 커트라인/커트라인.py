import sys

n,k=map(int,sys.stdin.readline().split())
cut=0
score=list(map(int,sys.stdin.readline().split()))

cut=int(max(score))

score.remove(cut)

for i in range(k-1):
    cut=int(max(score))
    score.remove(cut)
print(cut)