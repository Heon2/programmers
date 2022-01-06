def solution(phone_book):       #["119", "97674223", "1195524421"]
    phone_book.sort()           #["119", "1195524421", "97674223"]
    for i in range(len(phone_book)-1): #119, 1195524421
        if(phone_book[i]==phone_book[i+1][0:len(phone_book[i])]):   #slice는 범위를 넘기면 마지막까지 출력
            answer = False
            return answer
    
    answer = True
    return answer

    '''
    다른풀이
    def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
    '''