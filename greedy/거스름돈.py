num = int(input())
count = 0

array = [500, 100, 50, 10]

for i in array:
    count += num//i
    num %= i

print(count)
