num = input()  # 02984
result = int(num[0])

for i in range(int(len(num))-1):  # (((((0+2)*9)*8)*4)
    if(result < 2 or int(num[i+1]) < 2):  # 연산하는 수가 0 or 1이면 덧셈
        result = result+int(num[i+1])
    else:
        result *= int(num[i+1])

print(result)
