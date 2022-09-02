import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

M = list(map(int, input().split()))
for i in range(M[0], M[1]+1):
    if is_prime(i):
        print(i)