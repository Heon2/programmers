num = int(input())
dp = []
dp.append(1)  # 피보나치 1번
dp.append(1)  # 피보나치 2번

for i in range(2, num):
    dp.append(dp[i-1]+dp[i-2])

print(dp[num-1])
