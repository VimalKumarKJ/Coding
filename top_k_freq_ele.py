nums = [1,2,2,2,4]
k = 2

def kfrqele(nums, k):
    rec = {}
    count = [[] for i in range(len(nums) + 1)]
    for i in nums:
        rec[i] = 1 + rec.get(i, 0)
    res = []
    for ele, freq in count.items():
        count[freq].append(ele)
    for freq in range(len(count) - 1, 0, -1):
        for i in count[freq]:
            res.append(i)
            if len(res) == k:
                print(res)
                break
        
kfrqele(nums, k)