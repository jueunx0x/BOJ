def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    # 1) 교집합 제거
    both = lost_set & reserve_set #교집합
    lost_set -= both #교집합 제거
    reserve_set -= both # 교집합 제거

    # 2) 그리디: 작은 번호부터 처리
    for i in sorted(lost_set):
        if i - 1 in reserve_set:
            reserve_set.remove(i - 1)
            lost_set.remove(i)
        elif i + 1 in reserve_set:
            reserve_set.remove(i + 1)
            lost_set.remove(i)
        else:
            pass

    return n - len(lost_set)