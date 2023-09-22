def stringfrq(s):
    rec = {}
    res = []
    for i in s:
        if i in rec:
            rec[i] += 1
        else:
            rec[i] = 1
    
    for key, val in rec.items():
        res.append(f"{key}{val}")
    res = "".join(map(str, res))
    return res

s = "aabbcc"
print(stringfrq(s))