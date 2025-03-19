def linearSearch(arr: [], n: int, k: int):
    for i in range(n):
        if arr[i] == k:
            return i
        

print(linearSearch([1,2,3,4,5], 5, 2))