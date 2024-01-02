while True:
    try :
        print(input())#sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴하기 때문에 input으로 처리 
    except EOFError: #입력값이 없어지는 상황
        break