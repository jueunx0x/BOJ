from collections import Counter
import sys
N=int(sys.stdin.readline())
card_arr=[]
search_M=[]
card_arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
search_M=(list(map(int,sys.stdin.readline().split())))
count= Counter(card_arr)
for i in search_M:
    if(i in count):
        print(count[i],end=' ')
    else:
        print(0,end=' ')
