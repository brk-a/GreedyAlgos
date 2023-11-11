# highest product

### the problem
there are N integers. find the highest product possible from only three ints

constraints:
* 3 <= N <= 5e5

### test cases
* [1, 2, 3, 4]
    * N = 4
    * highest product is 24, ie, 4 * 3 * 2
* [0, -1, 10, 7, 5]
    * N = 5
    * highest product is 350, ie, 10 * 7 * 5
* [-5, -2, -1, 0, 0, 3, 4, 5]
    * N = 8
    * highest product is 60, ie, 3 * 4 * 5
> **Pattern 1: take the three highest numbers in a sorted array**
* [-5, -2, -1, 0, 0, 1, 1, 5]
    * N = 8
    * highest product is 50, ie, -5 * -2 * 5
> **Pattern 2: take the two lowest and the highest numbers in a sorted array**

### complexity

### optimisation

### code