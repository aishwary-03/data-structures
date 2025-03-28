def longestSubarrayWithSumK(a: [int], k: int) -> int:
    sum = 0
    start = 0
    end = -1
    maxL = 0
    n = len(a)
    while start < n:
        while end + 1 < n and sum + a[end + 1] <= k:
            sum += a[end + 1]
            end += 1
        if sum == k:
            maxL = max(maxL, end - start + 1) 
        sum -= a[start]
        start += 1
    return maxL

print(longestSubarrayWithSumK([2,3,5],5))