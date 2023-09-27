s ="helloprograming"
n = 7
ans = ""
mid_pt = len(s) // 2 # midpt = 2
left = mid_pt 
right = mid_pt
i = 1
while i < n and left > 0 and right < len(s):
    left -= 1
    i += 1
    right += 1
    i += 1
ans = s[left:right+1]
res = s[:left] + ans[::-1] + s[right+1:]
print(res)



