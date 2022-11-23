import sys
def combination(n,m):
    mul=1
    c_mul=1
    M_N_mul=1
    if n == 0:
        return mul

    for i in range(1,m+1):
        mul*=i

    for i in range(1,n+1):
        c_mul*=i
    for i in range(1,m-n+1):
        M_N_mul*=i

    return mul/(c_mul*M_N_mul)

T=int(sys.stdin.readline())
for i in range(0,T):
    m,n=map(int,sys.stdin.readline().split())

    answer=combination(m,n)
    print(int(answer))