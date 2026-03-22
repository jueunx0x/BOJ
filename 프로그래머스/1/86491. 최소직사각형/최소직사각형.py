def solution(sizes):
    max_w = []
    max_h = []
    
    answer = 0
        
    for w,h in sizes:
        max_w.append(max(w,h))
        max_h.append(min(w,h))
        
    print(max(max_w),max(max_h))
    answer = max(max_w) * max(max_h)

    return answer