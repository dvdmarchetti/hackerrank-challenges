#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    A = Counter(a)
    B = Counter(b)

    common = A & B

    removal = (A - common) + (B - common)
    return sum(removal.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
