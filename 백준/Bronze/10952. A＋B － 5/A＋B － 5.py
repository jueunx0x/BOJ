import sys
A,B=map(int,sys.stdin.readline().split())
while A>0 and B<10 and A!=0 and B!=0:
    try :
        SUM=A+B
        print(SUM)
        A, B = map(int, sys.stdin.readline().split())
    except: break