while 1 :
    a = input()
    arr_4949 = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            arr_4949.append(i)
        elif i == ']' :
            if len(arr_4949) != 0 and arr_4949[-1] == '[' :
                arr_4949.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else :
                arr_4949.append(']')
                break
        elif i == ')' :
            if len(arr_4949) != 0 and arr_4949[-1] == '(' :
                arr_4949.pop()
            else :
                arr_4949.append(')')
                break
    if len(arr_4949) == 0 :
        print('yes')
    else :
        print('no')