def getSingleElement(arr : list[int]) -> int:
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[i + 1]:
            return arr[i]
        i = i + 2
    return arr[-1]    

print(getSingleElement([1, 1, 2, 3, 3, 4, 4]))  