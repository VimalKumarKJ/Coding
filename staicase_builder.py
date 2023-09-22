num = 10

for i in range(1, num):
    num = num - i
    if num == 0:
        print(i)
        break
    elif num < 0:
        print(i-1)

    