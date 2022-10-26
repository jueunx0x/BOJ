import sys
median=0

while True:
    x,y,z=map(int,sys.stdin.readline().split())
    if(x==0 and y==0 and z==0):
        break

    if x<max(x,y,z) and x>min(x,y,z):
        median=x
    elif y<max(x,y,z) and y>min(x,y,z):
        median=y
    elif z<max(x,y,z) and z>min(x,y,z):
        median=z
    if max(x,y,z)**2 == median**2+min(x,y,z)**2:
        print("right")
    else:
        print("wrong")