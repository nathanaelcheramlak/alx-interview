#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def calcFactorial(num):
    if num <= 0:
        return 1
    return num * calcFactorial(num - 1)

def pascal_triangle(n):
    if n <= 0:
        return []
    for line in range(n):
        container = list()
        lineFactorial = calcFactorial(line)
        for item in range(line + 1):
            itemFactorial = calcFactorial(item)
            combinedFactorial = calcFactorial(line - item)

            final = int(lineFactorial / (itemFactorial * combinedFactorial))
            container.append(final)
        
        print(container)
