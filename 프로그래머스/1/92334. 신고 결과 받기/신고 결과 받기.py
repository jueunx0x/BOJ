#이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k
def solution(id_list,report,k):
    answer=[0]*len(id_list)
    reports={x:0 for x in id_list}
    
    print(answer,reports)
    for r in set(report):
        reports[r.split()[1]]+=1
    print(reports)
    for r in set(report):
        if reports[r.split()[1]]>=k:
            answer[id_list.index(r.split()[0])]+=1
        
    return answer