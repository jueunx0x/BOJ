def solution(name):
    n = len(name)
    # 1) 상하 이동(알파벳 변경)
    answer = 0
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

    # 2) 좌우 이동(커서 이동)
    move = n - 1  # 기본: 오른쪽으로 쭉 끝까지

    for i in range(n):
        next = i + 1
        # i 다음부터 연속된 A 구간 스킵
        while next < n and name[next] == 'A':
            next += 1

        # i에서 턴하는 두 가지 경우 중 최소
        move = min(move, i * 2 + (n - next), i + 2 * (n - next))

    return answer + move