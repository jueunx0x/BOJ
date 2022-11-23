import sys
def factorial(n):
    mul=1
    if n == 0:
        return mul

    for i in range(1,n+1):
        mul*=i
    return mul

n,k=map(int,sys.stdin.readline().split())

answer=factorial(n)//(factorial(k)*factorial(n-k))
print(answer%10007)