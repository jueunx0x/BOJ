import sys
N=int(sys.stdin.readline())
for i in range(1,2*N+1):
    if i * 2 <= 2 * N:
     print("*"*i+" "*(2*N-i*2)+"*"*i)
    else:
        print("*"*(2*N-i)+" "*(2*i-2*N)+"*"*(2*N-i))