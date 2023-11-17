# mice to holes

### the problem
there are N mice and N holes. a mouse takes one
minute to travel one unit left or right

what is the least time it takes the mice to get
into ther respective holes?

constraints
* 1 <= N <= 1e5
* -1e9 <- A[i] <= B[j] <= 1e9

### test cases
* [3, 2, -4], [0, -2, 4]
    * output: 2
        * first array -> positions of mice
        * second array -> positions of holes
        * sort both in ascending order: [-4, 2, 3], [-2, 0, 4]
        * one-to-one correspondence between mouse and hole
            * -4 -> 2 : 2 steps
            * 2 -> 0 : 2 steps
            * 3 -> 4 : 1 step

### complexity

### optimisation
* sort both arrays
* use 1-1 correspondence
* this way, the mice never cross paths

### code
* see [7-mice_to_hole.py][def]

[def]: ./7-mice_to_holes.py