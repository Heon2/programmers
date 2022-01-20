import math
num = int(input())

for i in range(2, int(math.sqrt(num))+1):
    if(num % i == 0):
        result = False
        break
    result = True

if(result):
    print('소수입니다')
else:
    print('소수가 아닙니다')
