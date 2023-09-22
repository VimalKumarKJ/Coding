def file_management(size, files):
    rec = {}
    ans = []
    for i in files:
        if i in rec:
            uniq_name = f"{i}{rec[i]}"
            rec[i] += 1
        else:
            rec[i] = 1
            uniq_name = i
        ans.append(uniq_name)
    return ans

size = 5
files = ['vimal', 'vimal', 'sowmiya', 'vs']
print(file_management(size, files))
            