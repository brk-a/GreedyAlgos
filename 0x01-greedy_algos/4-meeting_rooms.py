def solution(A):
    """ solve the meeting rooms problem"""
    A = A if A and isinstance(a, list) else None
    if not A:
        print("pass a list of lists to the function")
        return

    data = [[(s, 1), (e, -1)] for (s, e) in A]
    data = [data[i][j] for i in range(len(data)) for j in range(2)]
    data.sort()

    curr = 0
    _max = o

    for _, j in data:
        curr += j
        _max = max(_max, curr)
    return _max