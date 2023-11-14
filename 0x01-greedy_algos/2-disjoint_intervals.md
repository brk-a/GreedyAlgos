# disjoint intervals

### the problem
there is a list of N closed intervals

find the length of the maximal set of mutually
disjoint intervals

constranits:
* 1 <= N <= 1e5 
    * list has between one and one lakh intervals, inclusive
* 1 <= A[i][0] <= A[i][1] <= 1e9
    * first element of interval is always less than the second
    * both are at least one and at most 100 crore 

### test cases
* [[1, 2], [2, 10], [4, 6]]
    * output: 2
    * the two are [1, 2] and [4, 6]
    * [2, 10] overlaps with [1, 2], therefore, is not included
* [[1, 2], [2, 10], [4, 6]]
    * output: 1
    * that is [2, 10]
    * [1, 2] and [4, 6] overlap with [2, 10], therefore, are not
    included
* [[1, 4], [2, 3], [4, 6], [8, 9]]
    * output: 3
    * that is [2, 3], [4, 6] and [8, 9]
    * **this, however is not the maximal set**
* [[1, 4], [2, 3], [4, 6], [8, 9]]
    * output: 2
    * that is [1, 4] and [8, 9]
    * **this, however is not the maximal set**
> **Pattern: intervals that end earlier lead to the maximal set**

### complexity

### optimisation
* sort the intervals by ascending order of ending element
* check if start of an interval is at most (<=) the previous interval's end
    *  if yes: continue
    * if no:
        * set previous start and end to current start and end
        * increase count of maximal set by one
return count of maximal set
### code
* see [2-disjoint_intervals.py][def]

[def]: ./2-disjoint_intervals.py