from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    temp = arr[0]
    i = 1
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n-1] = temp

arr = [1,2,3,4,5]

rotateArray(arr, 5)

print(arr)