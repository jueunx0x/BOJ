def change(m):
    return m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a").replace("B#","C").replace("E#","A")
    
    
def solution(m, musicinfos):
    answer = ''
    
    m = change(m)
    p = [] #2개에 모두 해당 멜로디가 들어있는 경우 비교 (플레이 길이 체크)
    n = [] #2개에 모두 해당 멜로디가 들어있고 플레이 길이도 같은 경우 비교 (순서 체크)
    for i in musicinfos:
        start,end,title,melody = i.split(",")
        
        h1,m1 = map(int,start.split(":"))
        h2,m2 = map(int,end.split(":"))
        
        time = (h2*60+m2) - (h1*60+m1)
        
        melody = change(melody)
        played = (melody * (time // len(melody))) + melody[:time % len(melody)]
        if(m in played):
            p.append(played)
            n.append(title)
            
    if len(n) > 0 :
        indexes = [i for i,v in enumerate(p) if v == max(p,key=len)]
        
        if(len(indexes) > 2):
            answer = n[p.index(p[0])]
        else:
            answer = n[p.index(max(p,key=len))]
            
        # print(answer,n[p.index(max(p))],p.index(max(p)))
    if answer == '':
        answer = '(None)'
    return answer