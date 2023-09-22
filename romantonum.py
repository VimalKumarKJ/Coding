roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500
}
s = "XIV"
ans = 0
prev = 0
for i in s:
    curr = roman[i]
    if curr < prev:
        ans -= curr
    else:
        ans += curr
    prev = curr
print(ans)
