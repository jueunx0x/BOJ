def solution(participant, completion):
    hash_map = {}

    for p in participant:
        hash_map[p] = hash_map.get(p, 0) + 1 #기본값 0 에 +1

    for c in completion:
        hash_map[c] -= 1 #이름으로 찾아서 -1하기

    for key in hash_map:
        if hash_map[key] == 1: #여전히 1이면 완주못함
            return key