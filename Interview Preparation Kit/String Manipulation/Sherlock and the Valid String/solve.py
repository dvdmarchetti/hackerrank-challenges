#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    frequencies = Counter(s)

    target, _ = Counter(frequencies.values()).most_common(1)[0]

    can_remove = True

    for _, f in frequencies.items():
        if f != target:
            if not can_remove or (f > 1 and f-1 != target):
                return 'NO'

            can_remove = False

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
