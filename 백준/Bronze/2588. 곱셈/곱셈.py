A=int(input())
B=int(input())
o=int (A*(B%10))
t=int (A*((B%100-B%10)//10))
h=int (A*(B//100))
print(o,t,h,A*B,sep="\n")