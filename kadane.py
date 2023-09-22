arr = [-2, -3, 4, -1, -2, 1, 5, -3]

max_so_far = -99999
max_sum = 0

for i in range(0, len(arr)):
    max_sum = max_sum + arr[i]
    if max_so_far < max_sum:
        max_so_far = max_sum
    if max_sum < 0:
        max_sum = 0
print(max_so_far)