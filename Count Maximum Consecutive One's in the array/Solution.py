def maximumConsectiveOnes(a: []) -> int:
    max = temp = 0
    for i in range(len(a)):
        if a[i] == 1:
            temp = temp + 1
        else:
            if temp > max: 
                max = temp
            temp = 0
    if temp > max: 
        max = temp        
    return max

print(maximumConsectiveOnes([1, 1, 0, 1, 1, 1]))