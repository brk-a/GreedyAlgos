def solution(A, B):
    """ solution to petrol station problem"""
    A = A if A and isinstance(A, list) else None
    B = B if B and isinstance(B, list) else None
    if not (A or B):
        print(f"pass to arrays of ints as args")
        return
    
    N = len(A)
    curr = start = 0

    for i, (p, c) in enumerate(zip(A*2, B*2)): #p -> petrol, c -> cost
        if i==start+N:
            return start
        
        curr += p - c

        if curr < 0:
            start = i + 1
            curr = 0
        
    return -1

    if __name__=="__main__":
        pass