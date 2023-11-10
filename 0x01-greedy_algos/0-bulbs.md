# bulbs

### the problem
there are N bulbs which are either on (1) or off (0). turning on the i*th* bulb causes all bulbs to its right to flip

find the minimum number of switches to turn so that all bulbs are on

constraints:
* 1 <= N <= 1e5
* A[i] = {0, 1}

### test cases
* [1, 0, 1] and cost = zero
    * first element is 1: continue
    * second element is 0: flip. array viz: [1, 1, 0] and cost = 1
    * third element is 0: flip. array viz: [1, 1, 1] and cost = 2
    * return 2

### complexity
* time comlexity is quadratic, O(N*N)
    * there are N bits and, potentially, N flips to the right of the ith bit
    * N time for N bits
* space complexity is constant, O(1)
    * we store cost variable only

### optimisation
* say we have an array viz: [0, 1, 0, 1, 1, 0, 1, 1]
    * N = 8
    * first bit is zero: flip. array viz: [1, 0, 1, 0, 0, 1, 0, 0] and cost = 1
    * second bit is zero: flip. array viz: [1, 1, 0, 1, 1, 0, 1, 1] and cost = 2
    * third bit is zero: flip. array viz: [1, 1, 1, 0, 0, 1, 0, 0] and cost = 3
    * fourth bit is zero: flip. array viz: [1, 1, 1, 1, 1, 0, 1, 1] and cost = 4
    * fifth bit is 1: continue
    * sixth bit is zero: flip. array viz: [1, 1, 1, 1, 1, 1, 0, 0] and cost = 5
    * seventh bit is zero: flip. array viz: [1, 1, 1, 1, 1, 1, 1, 1] and cost = 6
    * eighth bit is 1: continue
    * return  6
* notice how everything to the right of the bit under consideration is the same every two flips
    * in other words, everything to the right of the bit under consideration follows and even-odd pattern w.r.t cost
* take a random bit, b, in the array
    * is the cost even?
        * yes: bit remains as is (b = b)
        * no: bit is flipped (b = !b)

### code
see [0-bulbs.py][def]

[def]: ./0-bulbs.py