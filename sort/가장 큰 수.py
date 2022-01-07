def solution(numbers):  # [6, 10, 2] / [3, 30, 34, 5, 9]
    numbers = list(map(str, numbers))  # 배열을 string으로 변환
    for i in range(len(numbers)):  # 2,3번째 숫자도 고려해야 하기때문에
        numbers[i] = numbers[i]*3  # 3->333,34->343434

    numbers.sort(reverse=True)  # [6, 2, 10] / [9, 5, 34, 3, 30]

    for i in range(len(numbers)):  # 333->3 으로 변환
        numbers[i] = numbers[i][0:int(len(numbers[i])/3)]

    # [0,0,0]의 경우 000이 반환되므로 int로 변환후 다시 str로 변환
    answer = str(int(('').join(numbers)))
    return answer


# 다른 풀이
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
'''
