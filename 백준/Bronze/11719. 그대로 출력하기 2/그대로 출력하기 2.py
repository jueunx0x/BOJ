while True:
    try :
        print(input())
    except EOFError: #입력값이 없어지는 상황
        break