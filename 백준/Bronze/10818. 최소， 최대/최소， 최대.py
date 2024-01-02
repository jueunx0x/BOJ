import sys
T = int(input())
T_list = list(map(int,sys.stdin.readline().split()))

print(min(T_list),max(T_list))