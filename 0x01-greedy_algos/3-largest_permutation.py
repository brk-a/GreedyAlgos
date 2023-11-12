def largestPermutation(A, B):
    """find the largest permutation possible"""
    A = A if A and isinstance(A, list) else None
    B = B if B and isinstance(B, int) else None
    if not A or not B:
        print("pass a list as the first arg and an int as the second arg")
        return

    i = 0
    _max = len(A)
    d = {x: i for i, x in enumerate(A)}

    while B and i<len(A):
        j = d[_max]
        if i==j:
            pass
        else:
            B -= 1
            A[i], A[j] = A[j], A[i]
            d[A[i]], d[A[j]] = d[A[j]], d[A[i]]
        
        i += 1
        _max -= 1
    
    return A

if __name__=="__main__":
    pass