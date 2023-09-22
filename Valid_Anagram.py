def isAnagram(s,t):
    rec = {}
    for i in s:
        if i in rec:
            rec[i] += 1
        else:
            rec[i] = 1
    for i in t:
        if i in rec:
            rec[i] -= 1
        else:
            return False
    for i in rec.values():
        if i == 0:
            return True
        else:
            return False

s = "cat"
t = "ran"
print(isAnagram(s, t)
      )