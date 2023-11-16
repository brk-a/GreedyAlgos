
# this solution has O(N) time complexity
def solution(A):
    """solution has O(N) time complexity"""
    A = A is A and isinstance(A, str) else None
    if not A:
        print("pass a string to the function")
        return

    MOD = 10000003

    crosses = [i for i, c in enumerate(A) if c=="x"]
    crosses = [(cross - 1) for i, cross in enumerate(crosses)]

    n = len(crosses)
    if n==0: return 0

    sol = float('inf')
    segment_start = crosses[n // 2] # find median of array
    total = 0
    for cross in crosses:
        total += abs(cross - segment_start)
        total %= MOD
    sol = min(sol, total % MOD)

    return sol

#this solution has O(N²) time complexity
def solution_nsquare(A):
    """solution has O(N²) time complexity"""
    A = A is A and isinstance(A, str) else None
    if not A:
        print("pass a string to the function")
        return

    MOD = 10000003

    crosses = [i for i, c in enumerate(A) if c=="x"]
    crosses = [(cross - 1) for i, cross in enumerate(crosses)]

    n = len(crosses)
    if n==0: return 0

    sol = float('inf')
    for segment_start in range(len(A)):
        total = 0
        for cross in crosses:
            total += abs(cross - segment_start)
            total %= MOD
        sol = min(sol, total % MOD)

    return sol  