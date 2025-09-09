def solution(friends, gifts):
    answer = 0
    giftFromToGraph = [[0]*len(friends) for _ in range(len(friends))]
    giftCount = [0] * len(friends)
    receiveCount = [0] * len(friends)
    # print(giftFromToGraph)
    for i in gifts:
        giftFrom,giftTo = i.split()
        idx_from = friends.index(giftFrom)
        idx_to = friends.index(giftTo)
        
        #주고 받은 선물 지수 지표
        giftFromToGraph[idx_from][idx_to] += 1 

    for i in range(len(friends)):
        for j in range(len(friends)):
            #선물 지수
            giftCount[i] += giftFromToGraph[i][j] - giftFromToGraph[j][i]
            
    for i in range(len(friends)):
        for j in range(len(friends)):
            maxCnt = max(giftFromToGraph[i][j],giftFromToGraph[j][i])
            if (maxCnt == giftFromToGraph[i][j] and giftFromToGraph[i][j] != giftFromToGraph[j][i]):
                receiveCount[i] += 1
            elif maxCnt == 0 and giftCount[i] > giftCount[j]:
                receiveCount[i] += 1
            elif giftFromToGraph[i][j] == giftFromToGraph[j][i] and giftCount[i] > giftCount[j]:
                receiveCount[i] += 1
    print(giftCount,receiveCount)
    answer = max(receiveCount)
    return answer