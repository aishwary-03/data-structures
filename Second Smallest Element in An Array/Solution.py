from math import *

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    min = secondMin = float(inf);
    for ele in a:
        if ele < min:
            secondMin = min;
            min = ele;
        elif ele < secondMin and secondMin != min:
            secondMin = ele;
    return secondMin;

secondSmallestElement = getSecondOrderElements(6, [8,2,5,-1,-4,3]);

print(secondSmallestElement);