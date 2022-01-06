array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands): #[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = []     #[5, 6, 3]
    for i in range(len(commands)):
        list = array[commands[i][0]-1:commands[i][1]]   #list = [5,2,6,3], [6], [1, 5, 2, 6, 3, 7, 4]
        list.sort()     #[2, 3, 5, 6]
        answer.append(list[commands[i][2]-1])
    return answer

print(solution(array, commands))

#다른 풀이
'''
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
'''