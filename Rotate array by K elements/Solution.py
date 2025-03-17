from sys import *
from collections import *
from math import *

def reverse(arr: [], start: int, end: int):
    while start < end:    
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotateArray(arr: [], n: int, k: int) -> []:
    reverse(arr, k , n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, 0 , n - 1)
    
arr = [1,2,3,4,5]

rotateArray(arr, 5, 3)

print(arr)