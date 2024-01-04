import sys
T = int(sys.stdin.readline())

for i in range (0,T):
    n = int(sys.stdin.readline())
    dp = [0, 1, 2, 4]
    for j in range(4,n+1):
        dp.append(dp[j-3]+dp[j-2]+dp[j-1])
    print(dp[n])