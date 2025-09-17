from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cacheDeque = deque()
    temp = 0
    
    totalTime = 0
    if cacheSize == 0 :
        answer = len(cities) * 5
    else:
        for i in cities:
            i = i.lower()
            
            if i in cacheDeque:
                totalTime+=1
                cacheDeque.remove(i)
                cacheDeque.append(i)
                
            else:
                if len(cacheDeque) == cacheSize:
                    cacheDeque.popleft()
                totalTime += 5
                cacheDeque.append(i)
                
        answer = totalTime
    return answer