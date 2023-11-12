# largest permutation

### the problem
there is an array, A, of a random permutation of numbers from 1 to N. you have B, the number of swaps in A that you can make

find the largest permutation possible

constraints:
* 1 <= N <= 1e6
* 1 <= B <= 1e9

### test cases
* A = [1, 3, 2], B = 1
    * output: [3, 1, 2]
    * N = 3
    * swap 1 and 3 since you can make only 1 swap
* A = [1, 2, 3, 4], B = 1
    * output: [4, 1, 2, 3]
    * N = 4
    * swap 1 and 4 since you can make only 1 swap
* A = [ 3, 2, 4, 1, 5], B = 3
    * output: [5, 4, 3, 1, 2]
    * N = 5
    * swap 5 and 3 then 4 and 2 then 3 and 2 since you can make 3 swaps

> **pattern: place the highest-valued number that is to the right of the number at the position of interest**

### complexity

### optimisation

### code
* see [3-largest_permutation.py][def]
    * use `i` as a pointer to traverse array `A` L-R
    * `_max` is the length of A. use it to traverse A R-L
    * `d` contains key-value pairs; the keys are the elements of A and the values are the respective positions/indexes of said elements
    * set up a loop that runs as long as the following are true
        * `B` is non-zero
        * the current index, i, is less than the length of A
    * inside the loop
        * set `j` as the value of d at key *_max* 
        * check if i is equal to j
            * equal: do nothing
            * not equal
                * reduce B by 1
                * swap the elements at positions i and j in A
                * swap the values of keys `A[i]` and `A[j]` in d
        * increase i by 1
        * reduce _max by 1
    * return A which is, now, sorted
        

[def]: ./3-largest_permutation.py