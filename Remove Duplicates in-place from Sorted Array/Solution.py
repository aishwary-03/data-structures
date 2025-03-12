def removeDuplicates(arr,n):
    i = 0
    for j in range(1, n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

print(removeDuplicates([1,2,2,3,4,5], 6))
