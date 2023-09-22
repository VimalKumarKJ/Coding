def dup_arr(arr):
    rec = {}
    for i in arr:
        if i in rec:
            rec[i] += 1
        else:
            rec[i] = 1
    if max(rec.values()) > 1:
        return True
    return False

arr = [1,1,2,3]
print(dup_arr(arr))