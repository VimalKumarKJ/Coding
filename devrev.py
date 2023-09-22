def prime_encryption(num):
    res = []
    vowels = "aeiou"
    consonents = "bcdfg"
    v, c = 0, 0
    prime = "2357"
    num_set = sorted(set(num))
    
    for i in num_set:
        if i in prime:
            res.append(vowels[v])
            v+=1
        else:
            res.append(consonents[c])
            c+=1
    for i in num:
        print(res[num_set.index(i)], end="")
num = "123412"
prime_encryption(num)
        