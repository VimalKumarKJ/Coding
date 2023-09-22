def two_sum(arr, target):
    ans = []
    rec = {}
    for i in range(len(arr)):
        req_num = target - arr[i]
        if req_num in rec:
            return [rec[req_num], i]
        rec[arr[i]] = i

arr = [1,2,3,4]
target = 5
print(two_sum(arr, target))
    
        