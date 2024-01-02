import sys
T=int(sys.stdin.readline())
for x in range(1,T+1):
    A,B=map(int,sys.stdin.readline().split())
    if A>0 and B<10:
        print(f'Case #{x}: {A} + {B} = {A+B}')