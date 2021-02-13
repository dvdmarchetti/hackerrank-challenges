#!/bin/python3

import itertools
import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    m = math.inf
    arr = sorted(arr)

    for x in range(len(arr) - 1):
        if abs(arr[x]-arr[x+1]) < m:
            m = abs(arr[x]-arr[x+1])

    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
