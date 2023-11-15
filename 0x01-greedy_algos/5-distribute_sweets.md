# distribute sweets

### the problem
N children stand in a line. each has a rating. sweets
are distributed viz:
    - each get at least one
    - those with higher ratings than their neighbours get
    more
find the minimum #sweets required

constraints
* 1 <= N <= 1e5

### test cases
* [1, 3, 7, 1]
* output: 7
    * N = 4; each gets one. #sweets = 4
    * rating 3 > 1: give sweet to child rated 3. #sweets = 5
    * rating 7 > 3: give sweet to child rated 7. #sweets = 6
    * rating 7 > 1: give sweet to child rated 7. #sweets = 7
    * return 7
* [1, 7, 4, 3, 1]
* output: 11
    * N = 5; each gets one. #sweets = 5
    * rating 7 > 1: give sweet to child rated 7. #sweets = 6
    * rating 7 > 4: give sweet to child rated 7. #sweets = 7
    * rating 4 > 3: give sweet to child rated 4. #sweets = 8
    * rating 3 > 1: give sweet to child rated 3. #sweets = 9
    * rating 4 > 3: give sweet to child rated 4. #sweets = 10
    * rating 7 > 4: give sweet to child rated 7. #sweets = 11
    * return 11

> > **pattern: if rating[i] > rating[i-1] sweets[i-1]++ else sweets = 1**
> > **pattern: if rating[i] > rating[i+1] sweets[i+1]++ else pass**

**optimisation**
* [1, 2, 7, 4, 3, 3, 1]
* output: 13
    * N = 7
    * sort in ascending order
        * [1, 1, 2, 3, 3, 4, 7]
    * position 0, rating = 1: give one sweet. #sweets = 1
    * position 1, rating = 1: same rating as previous. rating 1 gets one sweet. #sweets = 2
    * position 2, rating = 2: give one more sweet. rating 2 gets 2 sweets. #sweets = 4
    * position 3, rating = 3: give one more sweet. rating 3 gets 3 sweets. #sweets = 7
    * position 4, rating = 3: same rating as previous. rating 3 gets 1 sweet. #sweets = 8
    * position 5, rating = 4: give one more sweet. rating 4 gets 2 sweets. #sweets = 10
    * position 6, rating = 7: give one more sweet. rating 7 gets 3 sweets. #sweets = 13
    * return 13

### complexity

### optimisation
* iterating L-R then R-L will not solve the problem efficiently
* need to sort in ascending order then iterate L-R
* give one sweet to lowest rating. check if next rating == or > current
    * if next == current: give one sweet sweet to next
    * if next > current: give one *more* sweet to next
* have a sweet counter. adjust it when sweets are given out
* return sweet counter 

### code
see [5-distribute_sweets.py][def]

[def]: ./5-distribute_sweets.py