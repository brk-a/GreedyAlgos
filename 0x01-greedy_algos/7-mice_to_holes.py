def solution(A, B):
    """ solution to mice-in-holes problem"""
    A = A if A and isinstance(A, list) else None
    B = B if B and isinstance(B, list) else None
    if not A or not B:
        print(f"pass two lists as args to the fn")
        return

    A.sort()
    B.sort()

    sol = 0
    for a, b in zip(a, b):
        sol =  max(sol, abs(a - b))
    
    return sol

if __name__=="__main__":
    pass