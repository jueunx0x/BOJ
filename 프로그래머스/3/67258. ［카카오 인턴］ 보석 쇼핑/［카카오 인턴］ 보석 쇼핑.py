# def solution(gems):

#     start,end = 0,0
#     result = []
    
#     for i in range(len(gems)):
#         unique = list(dict.fromkeys(gems))
#         if gems[i] in unique:
#             idx = i
#             for j in range(idx,len(gems)):
#                 if gems[j] in unique:
#                     unique.remove(gems[j])
#                 if len(unique) == 0:
#                     start = idx 
#                     end = j
#                     if len(result) == 0 :
#                         result = [start+1,end+1]
#                     if len(result) > 0 and end - start < result[1] - result[0]:
#                         result = [start+1,end+1]
#                     break
#     # print(result)

#     return result


def solution(gems):
    n = len(gems)
    kinds = len(set(gems))   # 전체 보석 종류 수
    counter = {}
    answer = [0, n-1]        # 초기값: 전체 구간
    
    left = 0
    for right in range(n):
        # counter dict에 보석있으면 그 값에 +1 없으면 0반환->+1 
        counter[gems[right]] = counter.get(gems[right], 0) + 1
        
        # 현재 구간이 모든 보석을 포함할 때
        while len(counter) == kinds:
            # 최소 구간 갱신
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            
            # 왼쪽 보석 제거 시도
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
    

    return [answer[0] + 1, answer[1] + 1]