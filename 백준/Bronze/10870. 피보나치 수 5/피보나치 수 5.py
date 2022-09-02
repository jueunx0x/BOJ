def pivo(n):
    pivo = {}
    pivo[0]=0
    pivo[1]=1


    for i in range(2, n + 1):
        pivo[i] = pivo[i - 1] + pivo[i - 2]

    return pivo[n]

n=int(input())
print(pivo(n))