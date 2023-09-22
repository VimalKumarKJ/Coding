num = [1,3,5,4]
n = len(num)
i = n-2 # 3
while i >= 0 and num[i] >= num[i+1]:
    i -= 1

if i < 0:
    num.sort(reverse=True)
else:
    for j in range(len(num)-1,-1,-1):
        if num[j] > num[i]:
            break
    num[i], num[j] = num[j], num[i]
left, right = i+1, n-1
while left < right:
    num[left], num[right] = num[right], num[left]
    left+=1
    right-=1

print(num)
