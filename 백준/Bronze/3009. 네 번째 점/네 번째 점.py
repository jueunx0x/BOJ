import sys
x_list=[]
y_list=[]

answer_x=0
answer_y=0
for i in range(0,3):
    x,y = map(int,sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

for i in range(0,3):
    if x_list.count(x_list[i])==1:
        answer_x=x_list[i]
    if y_list.count(y_list[i])==1:
        answer_y=y_list[i]

print(answer_x,answer_y)