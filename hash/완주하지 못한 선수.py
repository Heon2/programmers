def solution(participant, completion): #participant = ["leo", "kiki", "eden"], completion = ["eden", "kiki"]
    participant.sort()             #['eden', 'kiki', 'leo']
    completion.sort()              #['eden', 'kiki']
    completion.append('')          #['eden', 'kiki', '']
    for p,c in zip(participant,completion):
        if p!=c:
            return p