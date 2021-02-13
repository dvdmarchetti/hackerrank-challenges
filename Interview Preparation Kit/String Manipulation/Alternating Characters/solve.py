#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0

    i = 0
    L = len(s)
    while i < L:
        j = 1
        while i+j < L and s[i] == s[i+j]:
            j += 1

        if j > 0:
            deletions += j - 1

        i += j

    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
