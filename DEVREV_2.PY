def last_id(string):
    res = set()
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            res.add(string[i:j])
    res = list(res)
    res.sort()
    # print(res)
    return res[-1]  

string = "abcde"
print(last_id(string))