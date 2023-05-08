import sys
n = int(sys.stdin.readline())
sum = 0
arr_n=[]
for i in range(0,n):
    j= int(sys.stdin.readline())
    if j == 0:
        arr_n.pop()
    else: arr_n.append(j)

if len(arr_n)==0: print(0)
else :
    for i in arr_n:
        sum+=i
    print(sum)