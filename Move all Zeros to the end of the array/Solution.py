def moveZeros(n: int,  a: [int]) -> [int]:
    i = j = 0
    while j < n:
        if a[i] == 0 and a[j] == 0:
            j += 1
        elif a[i] == 0 and a[j] != 0:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    return a

print(moveZeros(7, [1,2,3,0,3,2,1]))



