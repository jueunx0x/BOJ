from collections import Counter
import sys
hear,see=map(int,sys.stdin.readline().split())
hear_list=[0]*(hear)
hear_list=set()
for i in range(hear):
    hear_list.add(input())


see_list=[0]*see

see_list=set()
for i in range(see):
    see_list.add(input())


total_list=sorted(list(hear_list & see_list))
count=Counter(total_list)

num=0
print_list=[]
for i in total_list:
    if i in count:
        num+=int(count[i])
        print_list.append(i)
print(num)
for i in print_list:
    print(i)