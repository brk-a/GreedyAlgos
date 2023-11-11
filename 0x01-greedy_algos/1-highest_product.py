def highestProduct(A):
    """return the highest product of any three elements given an array of ints"""
    A = A if A and isinstance(A, list) else None
    if not A:
        print("Please pass a list of ints to the function")
        return        
        
    A = sorted(A)

    highest3 = A[-1] * A[-2] * A[-3]
    lowest2highest1 = A[0] * A[1] * A[-1]

    return max(highest3, lowest2highest1)

if __name__=="__main__":
    pass
