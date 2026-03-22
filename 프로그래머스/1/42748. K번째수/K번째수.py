def solution(array, commands):
    sort_arr = []
    answer = []
    location = 0
    for i in commands:
        sort_arr = array[i[0]-1:i[1]]
        sort_arr.sort()
        answer.append(sort_arr[i[2]-1])

    return answer