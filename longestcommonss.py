num = [5,4,11,1,16,8]
n = len(num)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if num[i] >= num[j] and dp[i] <= dp[j]+1:
            dp[i] = dp[j] + 1
print(max(dp))