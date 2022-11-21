A,B,C=map(int,input().split())


if A==B and A==C:
    money=10000+(A)*1000
elif A==B or B==C:
    money=1000+(B)*100
elif A==C:
    money = 1000 + (A) * 100
else:
    money=max(A,B,C)*100

print(money)