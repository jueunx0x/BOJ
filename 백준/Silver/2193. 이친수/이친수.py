import sys

t = int(input()) #자릿수 선언 
dp = [0] * (t + 1) #배열의 길이 선언 
dp[1] = 1 #이친수는 1로 시작해야하므로 첫째 자리에 1 삽입

for i in range(2,t+1): #점화식 사용
    dp[i] = dp[i-1]+dp[i-2]

print(dp[t]) #t자릿수의 이친수의 갯수 출력