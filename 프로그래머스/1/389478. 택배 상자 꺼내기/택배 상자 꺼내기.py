def solution(n, w, num):
    answer = 0
    # num이 위치한 층(row)
    row = (num - 1) // w
    idx = (num - 1) % w

    # 지그재그 열(column) 계산
    if row % 2 == 0:      # 왼 → 오
        col = idx
    else:                 # 오 → 왼
        col = w - 1 - idx

    # 마지막 층 정보
    last_row = (n - 1) // w
    last_cnt = n - last_row * w

    # 마지막 층에서 해당 column이 존재하는지 확인
    if last_row % 2 == 0:
        # 왼 → 오
        exists = col < last_cnt
    else:
        # 오 → 왼
        exists = col >= w - last_cnt

    # 가장 위에 있는 층
    top_row = last_row if exists else last_row - 1
    answer = top_row - row + 1
    return answer