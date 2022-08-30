M=int(input())
N=int(input())
sosu=[]
for i in range(M,N+1):
    for j in range(2,i+1):
        if i % j==0:
            if i==j:
                sosu.append(i)
            else:
                break
if len(sosu)>0:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
