import sys
from collections import Counter

N = int(sys.stdin.readline())
num = [0] * N
count = 0
for i in range(N):
    num[i] = int(sys.stdin.readline())
avg=sum(num) / len(num)
print(round(avg))
num.sort()
print(num[N // 2])  # 중간값

count = Counter(num)
tmp = count.most_common()

if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

print(max(num) - min(num))  # 범위