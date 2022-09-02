import math

k=123456*2+1
num_list=[1]*k
sum=0
for i in range (1,k):
    if i==1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j==0):
            num_list[i]=0
            break

while(True):
    n=int(input())
    if(n==0):
        break
    sum=0
    for i in range(n+1,2*n+1):
        sum+=num_list[i]
    print(sum)