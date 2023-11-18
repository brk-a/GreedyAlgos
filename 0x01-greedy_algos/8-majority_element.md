# majority element

### the problem
there is an array of intergers of size N. majority
element occurs with > \[N/2\] frequency

find the majority element

constraints
* 1 <= N <= 1e6

### test cases
* [3, 2, 2, 4, 2, 2]
    * output: 2
    * 2 occurs four times
        * 4 > \[6/2\]

### complexity
* trivial solution has linear time and space complexity
    * iterate over N items and create a hashmap (keys are
    unique elements in array and values are frequency of
    occurrence)
    * worst-case scenario: there is no key that statisfies
    the constraint and that each element appears once. iterate
    over  N keys

### optimisation
* back to basics: bits
* check the rightmost bit of each element. which bit occurs the
most? record it
* do the same for all othe bits of the elements
* the number formed by the bits recorded (L-R) is te majority element
* this approach results in constant space  and log-linear,
O(N * log(w)) time complexity (w is the bit size of the data type)

### code
* see [8-majority_element.py][def]

[def]: ./8-majority_element.py