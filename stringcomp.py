stri = "aaabbcccdde"
ans = ""
rec = {}
for i in stri:
    if i in rec:
        rec[i] += 1
    else:
        rec[i] = 1

for key, value in rec.items():
    ans += key + str(value)
print(rec)
print(ans)


