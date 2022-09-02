n=int(input())
num=[]

for i in range(0,n):
    num.append(int(input()))

num.sort()
for i in num:
    print(i)