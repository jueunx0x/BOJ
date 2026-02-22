def solution(wallet, bill):
    answer = 0
    while ((max(wallet) < max(bill)) or (min(wallet) < min(bill))):
        if(max(wallet) < max(bill)):
            max_bill = max(bill)
            max_idx = bill.index(max_bill)
            bill[max_idx] = max_bill // 2
            answer += 1

        elif (min(wallet) < min(bill)):
            max_bill = max(bill)
            max_idx = bill.index(max_bill)
            bill[max_idx] = max_bill // 2
            answer += 1
    return answer
