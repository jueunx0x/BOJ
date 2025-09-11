def solution(today, terms, privacies):
    answer = []
    termsDict,privaciesDict = {},{}

    
    #약정종류를 key로 유효기간 저장
    for i in terms:
        x,y = i.split()
        termsDict[x] = y
    
    idx = 0
    #index를 key로 개인정보수집일자와 약정종류 저장
    for i in privacies :
        x,y = i.split()
        privaciesDict[idx] = x,y
        idx += 1
        
    #약정별로 개인정보 수집 일자와 합한 날짜
    for i in privaciesDict:
        x,y = privaciesDict[i]
        for j in termsDict:
            if j == y:
                tyyyy,tmm,tdd = x.split('.')
                tyyyy,tmm,tdd = int(tyyyy),int(tmm),int(tdd)
                termDD = termsDict[j]
                
                termDD = int(termDD)
                #유효기간이이 12개월이 넘어가면 처리하는 로직
                if termDD >= 12 :
                    tyyyy += termDD//12
                    tmm += termDD%12
                else:
                    tmm += termDD%12
                
                #12보다 더 큰 경우 
                if tmm > 12:
                    tyyyy += tmm // 12
                    tmm = tmm % 12 
                
                yyyy,mm,dd = today.split('.')
                yyyy,mm,dd = int(yyyy),int(mm),int(dd)
                
                if yyyy > tyyyy:
                    answer.append(i+1)
                else:
                    if yyyy == tyyyy and mm > tmm:
                        answer.append(i+1)
                    else:
                        if yyyy == tyyyy and mm == tmm and dd >= tdd:
                            answer.append(i+1)
                
    return answer