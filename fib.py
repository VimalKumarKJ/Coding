# n = 4 -> 1 1 1 1 4 8 
n = 4
sum = 0
ans = []
while sum < n:
    ans.append(1)
    sum += 1

a, b = sum, n

for i in range(n):
    ans.append(a)
    a, b = b, a+b
print(ans)