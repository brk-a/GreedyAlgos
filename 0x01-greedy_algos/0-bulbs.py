#!/usr/bin/env python3

from sys import argv, exit

def bulbs(A):
    """solve bulbs problem"""
    A = A if isinstance(A, list) else None
    if not A:
        print("Please pass a list of bits")
        return
    
    cost = 0

    for b in A:
        if cost%2==0:
            b = b
        else:
            b = not b

        if b%2==1:
            continue
        else:
            cost += 1
    return cost

if __name__ == "__main__":
    pass
    # if len(argv)!=2:
    #     print("Usage: ./0-bulbs.py <list_of_bits>")
    #     exit(1)
    # A = argv[1]
    # cost = bulbs(A)
    # print(f"Cost of solving problem {A} is {cost}")