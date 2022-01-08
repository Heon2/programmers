def solution(citations):  # [3, 0, 6, 1, 5]
    answer = 0
    citations.sort()  # [0, 1, 3, 5, 6]

    for i in range(len(citations)):
        if(citations[i] >= (len(citations) - i)):  # 3>=3
            answer = len(citations) - i  # 5-2
            break

    return answer
