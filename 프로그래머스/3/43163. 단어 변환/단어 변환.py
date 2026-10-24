from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    q = deque([])
    count = 0
    
    if target not in words:
        return 0 # target이 없으면 변환 불가

    q.append((begin,answer)) #첫단어, 횟수
    
    while q:
        word,count = q.popleft()
        
        if target == word:
            answer+=count
            return answer
        
        for idx, candidate in enumerate(words):
            if visited[idx]:
                continue

            cnt = 0  # 후보 단어마다 새로 세기
            for a, b in zip(word, candidate):
                if a != b:
                    cnt += 1

            if cnt == 1:
                visited[idx] = True
                q.append((candidate, count + 1))


    return 0