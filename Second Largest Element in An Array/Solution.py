from sys import *
from collections import *
from math import *

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    max = secondMax = a[0];
    for ele in a:
        if ele > max:
            secondMax = max;
            max = ele;
        elif ele > secondMax and secondMax != max:
            secondMax = ele;
    return secondMax;

secondLargestElement = getSecondOrderElements(5, [1,2,3,4,5]);

print(secondLargestElement);