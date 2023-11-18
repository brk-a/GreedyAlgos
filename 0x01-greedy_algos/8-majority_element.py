from collections import Counter

def solutionTrivial(A):
    """trivial solution to majority element problem"""
    A = A if A and isinstance(A, list) else None
    if not A:
        print("pass a list of ints to the function")
        return
    
    return Counter(A).most_common(1)[0][0]

def solutionOptimised[A]:
    """optimised solution to majority element problem"""
    A = A if A and isinstance(A, list) else None
    if not A:
        print("pass a list of ints to the function")
        return

    n = len(A)
    sol = 0

    for b in range(32): #why 32? 32-bit int. change this to 64 etc when required
        ones = 0 #1s
        for num in A: #O(N)
            if(1<<b) & num:
                ones += 1

        if ones > n // 2:
            sol += (1 << b)
    
    return sol

if __name__=="__main__":
    pass