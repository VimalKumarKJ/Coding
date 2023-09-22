# Longest pallindrome substring without repetations

s = "abcbbcef"
rec = {}
max_s = 0
start = 0

# for i in range(len(s)):
#     if s[i] in rec and start <= rec[s[i]]:
#         start = rec[s[i]] + 1 #2-c
#     else:
#         max_s = max(max_s, (i - start) + 1)
#     rec[s[i]] = i
# print(max_s)

#variation - 2
for i in range(len(s)):
    if s[i] in rec and rec[s[i]] >= 2:
        while start < i and rec[s[i]] >= 2:
            rec[s[start]] -= 1
            start += 1
        rec[s[i]] = 1
    else:
        rec[s[i]] += rec.get(s[i], 0) + 1 #if rec is present gets s[i] else gets 0
    max_s = max(max_s, (i - start)+1)
print(max_s)
    