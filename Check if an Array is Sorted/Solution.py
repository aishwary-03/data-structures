from sys import *
from collections import *
from math import *

def isSorted(n: int,  a: [int]) -> int:
    for i in range(n-1):
        if a[i] > a[i+1]:
            return 0;
    return 1;

print(isSorted(3, [1,0,4]))