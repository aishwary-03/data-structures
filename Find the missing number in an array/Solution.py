from typing import *

def missingNumber(a : List[int], N : int) -> int:
    for i in range(1, N):
        if i not in a:
            return i
    return N    

print(missingNumber([2, 19,10, 1, 5, 3, 13, 18, 24, 23, 9, 22, 28, 25, 6, 27, 4, 20, 21, 26, 11, 8, 17, 15, 16, 12, 7, 14], 29))