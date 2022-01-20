import math
num = int(input())  # 2~num까지의 모든 수에 대하여 소수 판별
array = [True]*(num+1)

for i in range(2, int(math.sqrt(num))+1):
    if (array[i] == True):
        j = 2
        while(i*j <= num):
            array[i*j] = False
            j += 1

for i in range(2, num+1):
    if(array[i]):
        print(i, end=' ')
