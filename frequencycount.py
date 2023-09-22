def freqcount(arr, freq):
    rec = {}
    ans = []
    for i in arr:
        if i in rec:
            rec[i] += 1
        else:
            rec[i] = 1
    
    def desc_sort(item):
        return (-rec[item], - item)
    
    intermediate = sorted(rec.keys(), key = desc_sort)

    for i in intermediate:
        if rec[i] >= freq:
            ans.append(i)
    return " ".join(map(str, ans))

n = int(input())
arr = list(map(int, input().split()))
freq = int(input())

print(freqcount(arr, freq))