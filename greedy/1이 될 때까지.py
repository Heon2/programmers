num = int(input())
k = int(input())
count = 0
while(True):
    if(k == 1):  # 나누는 수가 1일경우 빼기만 -1만 수행
        count = num-1
        break
    if(num == 1):  # num이 1이면 탈출
        break
    if(num % k != 0):  # num이 k로 나누어 떨어지지 않을때
        num += -1
        count += 1
    else:  # num이 k로 나누어 떨이지면
        num //= k
        count += 1

print(count)

# 다른 풀이
'''
n, k = map(int,input().split())
count = 0

while True:
    target = (n//k)*k
    count += (n-target)
    n = target
    if(n<k):
        break
    n //= k
    count += 1

count += (n-1)
print(count)
'''
