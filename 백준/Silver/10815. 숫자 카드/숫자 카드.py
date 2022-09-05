import sys
N=int(sys.stdin.readline())
n_arr=set(list(map(int,sys.stdin.readline().split())))#상근이가 가진 카드는 출력이 필요 없으므로 중복 제거해줘도 무방함. 
M=int(sys.stdin.readline())
m_arr=list(map(int,sys.stdin.readline().split()))

for i in range(M):
    if(m_arr[i] in n_arr):
        print(1,end=' ')
    else:
        print(0,end=' ')