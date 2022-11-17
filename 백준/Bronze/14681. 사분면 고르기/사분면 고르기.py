X=int(input())
Y=int(input())
if X < -1000 or X > 1000:
    X = int(input())
elif Y < -1000 or Y > 1000:
    Y = int(input())
elif X > 0 and Y > 0 :
    print("1")
elif X < 0 and Y > 0:
    print("2")
elif X < 0 and Y < 0 :
    print("3")
else:
    print("4")