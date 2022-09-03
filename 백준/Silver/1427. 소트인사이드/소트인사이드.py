import sys
N=str(sys.stdin.readline())
reverse_list=[]
for i in N:
    reverse_list.append(i)

reverse_list.sort(reverse=True)
for i in reverse_list:
    print(i,end='')