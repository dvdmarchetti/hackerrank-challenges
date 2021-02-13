#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys


class UnionSet:
    def __init__(self):
        self.parent = {}
        self.sizes = {}
        self.max_size = 1

    def make_set(self, v):
        if v not in self.parent:
            self.parent[v] = v
            self.sizes[v] = 1

    def find_set(self, v):
        if v == self.parent[v]:
            return v

        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v];

    def union(self, source, target):
        source = self.find_set(source);
        target = self.find_set(target);

        if source != target:
            if self.sizes[source] < self.sizes[target]:
                source, target = target, source

            self.parent[target] = source
            self.sizes[source] += self.sizes[target]
            if self.sizes[source] > self.max_size:
                self.max_size = self.sizes[source]


def maxCircle(queries):
    A = UnionSet()
    output = []

    for source, target in queries:
        A.make_set(source)
        A.make_set(target)
        A.union(source, target)

        output.append(A.max_size)

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
