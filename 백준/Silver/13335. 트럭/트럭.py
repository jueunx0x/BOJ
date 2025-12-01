import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

# 다리 위 상태 (처음에는 전부 빈 칸 = 0)
bridge = deque([0] * w)

time = 0               # 흐른 시간
current_weight = 0     # 현재 다리 위 트럭 무게 합

# 대기 트럭이 있거나, 다리 위에 트럭이 남아 있는 동안 반복
while trucks or current_weight > 0:
    time += 1

    # 1. 한 칸 전진: 다리 맨 앞에서 나감
    left = bridge.popleft()
    current_weight -= left

    # 2. 새 트럭을 올릴 수 있으면 올림
    if trucks:
        if current_weight + trucks[0] <= L:
            next_truck = trucks.popleft()
            bridge.append(next_truck)
            current_weight += next_truck
        else:
            # 못 올라가면 빈 칸
            bridge.append(0)
    else:
        # 더 이상 올릴 트럭이 없으면 계속 0만 밀려감
        bridge.append(0)

print(time)
