#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    partials = [0] * (n+1)
    for query in queries:
        l, r, score = query
        partials[l] += score
        if r+1 < len(partials):
            partials[r+1] -= score

    current_max = 0
    candidate = 0
    for partial in partials:
        candidate += partial
        if candidate > current_max:
            current_max = candidate

    return current_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
