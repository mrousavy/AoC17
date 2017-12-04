#!/bin/python

def diff(line):
    return abs(max(line) - min(line))

def checksum(lines):
    sum = 0
    for line in lines:
        sum += diff(line)
    return sum


lines = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
print(str(checksum(lines)))

