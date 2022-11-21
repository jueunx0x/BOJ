import sys
def gcd(a, b):
    while(b != 0):
        n = a%b
        a = b
        b = n
    return a

N=int(sys.stdin.readline())
r_arr=list(map(int,sys.stdin.readline().split()))


for i in range(1,len(r_arr)):
    g=gcd(r_arr[0],r_arr[i])
    print('{0}/{1}'.format(r_arr[0] // g, r_arr[i] // g))