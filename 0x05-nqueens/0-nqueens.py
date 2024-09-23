#!/usr/bin/python3
from typing import List
from sys import argv, exit


"""
N queens puzzle is the challenge of placing N
"""


def NQueens(N: int) -> List[List[str]]:
    """ N queens puzzle is the challenge of placing N """
    cds = set() #previce queen location 
    postDIG = set() # r-c = constant
    negtDIG = set() # r+c = constant


def dealing_with_user() -> int:
    """ it will get data from user """
    list_from_user:list = argv

    if len(list_from_user) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        num = int(list_from_user[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if num < 4:
        print("N must be at least 4")
        exit(1)
    return num


if __name__ == "__main__":
    print(dealing_with_user())