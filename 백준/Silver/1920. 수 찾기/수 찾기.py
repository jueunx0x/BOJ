import sys

N = int(sys.stdin.readline())
N_arr = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_arr = list(map(int,sys.stdin.readline().split()))


N_arr.sort()
def binary_search(arr,target):
    left = 0
    right = int(len(arr) - 1)
    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

for i in range(M):
    result = binary_search(N_arr,M_arr[i])
    print(1) if result == True else print(0)
