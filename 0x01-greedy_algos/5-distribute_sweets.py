def solution(A):
    A = A if A and isinstance(A, list) else None
    if not A:
        print("pass a list of ints into the fn")
        return
    
    n = len(A)
    data = sorted((x, i) for x in enumerate(A))

    sweets = [1] * n

    for _, i in data:
        if i>0 and A[i]>A[i-1]:
            sweets[i] = max(sweets[i], sweets[i-1]+1)
        if i<n-1 and A[i]>A[i+1]:
            sweets[i] = max(sweets[i], sweets[i+1]+1)
    
    return sum(sweets)