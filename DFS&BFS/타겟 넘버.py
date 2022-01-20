# itertools 풀이
from itertools import product


def solution(numbers, target):
    plus_minus = list(product(['+', '-'], repeat=len(numbers)))
    answer = 0
    for i in range(len(plus_minus)):
        sum = 0
        for j, pm in enumerate(plus_minus[i]):
            if(pm == '+'):
                sum += numbers[j]
            else:
                sum -= numbers[j]
        if(sum == target):
            answer += 1
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

# DFS를 이용한 풀이
'''
answer = 0
def dfs(i,numbers,target,sum):
    global answer
    if(i==len(numbers) and sum == target):
        answer += 1
        return
    if(i==len(numbers)):
        return
    dfs(i+1,numbers,target,sum+numbers[i])
    dfs(i+1,numbers,target,sum-numbers[i])
    
def solution(numbers, target):
    global answer
    dfs(0,numbers,target,0)
    return answer
'''
