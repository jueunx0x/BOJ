import sys
n = int(sys.stdin.readline())

for i in range(0,n):
    n_str = str(sys.stdin.readline())
    sum = 0
    for i in list(n_str):
        if i =='(':
            sum+=1
        elif i==')':
            sum-=1
            if sum==-1:
                break

    if sum == 0:
        print('YES')
    else :
        print('NO')