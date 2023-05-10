arr_n = []
stack = []
temp = True
count = 1

n = int(input())
for i in range(n):
    m = int(input())
    while count <= m:
        arr_n.append(count)
        stack.append('+')
        count += 1
    if m == arr_n[-1]:
        arr_n.pop()
        stack.append('-')
    else :
        temp = False
        break
if temp == False:
    print('NO')
else:
    for i in stack:
        print(i)