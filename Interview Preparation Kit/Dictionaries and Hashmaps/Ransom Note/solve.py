#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_count = Counter(magazine)
    note_count = Counter(note)

    for word, count in note_count.items():
        if word not in magazine_count or count > magazine_count[word]:
            return 'No'

    return 'Yes'

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
