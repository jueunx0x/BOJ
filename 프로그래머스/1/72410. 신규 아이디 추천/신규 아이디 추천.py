def solution(new_id):
    #1단계
    new_id = new_id.lower()
    
    #2단계
    def solution2(new_id):
        new_id2 = ''
        for i in new_id:
            if i == '.' or i =='-' or i == '_' or i.isdigit() or i.islower():
                new_id2 += i
        return new_id2
    #3단계
    def solution3(new_id):
        while(new_id.find('...') > -1 or new_id.find('..') > -1):
            new_id = new_id.replace('...','.')
            new_id = new_id.replace('..','.')
        return new_id
    
    #4단계
    def solution4(new_id):
        new_id =new_id.lstrip('.')
        new_id = new_id.rstrip('.')
        return new_id
    
    
    new_id = solution2(new_id)
    new_id = solution3(new_id)
    new_id = solution4(new_id)
    #5단계 
    if new_id == '':
        new_id = 'a'
    #6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = solution4(new_id)
    #7단계
    if len(new_id) < 3:
        for i in range(3 - len(new_id)):
            new_id += new_id[len(new_id)-1]

    answer = new_id
    return answer