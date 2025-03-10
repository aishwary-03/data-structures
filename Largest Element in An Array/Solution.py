from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    max = arr[0];
    for ele in arr:
        if ele > max:
            max = ele;
    return max;

largest = largestElement([1,2,3,4,5,6,7,8], 5);

print(largest);