import sys
N=int(input())
arr=list(map(int,sys.stdin.readline().split()))

index_arr=sorted(set(arr))#중복 제거하여 순서대로 정렬

dic = {index_arr[i]:i for i in range (len(index_arr))}#해당 숫자와 각 숫자의 인덱스를 dic에 저장

for i in arr:
    print(dic[i],end=' ')