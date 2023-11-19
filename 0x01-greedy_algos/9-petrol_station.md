# petrol station

### the problem
there are N petrol stations along a circular route. each station,
i, has A[i] amount of petrol. travel from station i to staion i+1
costs B[i] amout of petrol

find the earliest station from where one can travel around the
entire circuit, else, return -1

constraints
* 1 <= N <= 1e6

### test cases
* N = 5, A = [3, 5, 2, 1, 7] and B = [4, 2, 1, 9, 1]. start at i = 4
    * output: 4
    * have a table viz:

    |index|0|1|2|3|4|
    |:---:|:---:|:---:|:---:|:---:|:---:|
    |petrol|3|5|2|1|7|
    |cost|4|2|1|9|1|
    |curr|5|8|9|1|6|

    * start at 4. you have 7 units of fuel. use one unit to get to i = zero; 6 units remain. add 3 at i = zero then use 4 to get to i=1; 5 units remain. add 5 units at i=1 then use 2 to get to i=2; 8 units remain. add 2 units at i=2 and use 1 to get to i=3; 9 units remain. add 1 unit at i=3 then use 9 units to get to i=4; one unit remains. job done

### complexity
* brute force takes O(N²) time and O(1) space
* optimisation takes O(N) time and near-constant space

### optimisation
* have a table viz:

    |index|0|1|2|3|4|5|6|7|8|9|
    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
    |petrol|3|5|2|1|7|3|5|2|1|7|
    |cost|4|2|1|9|1|4|2|1|9|1|
    |curr|||||||||||

    * simply repeat the columns (index zero is index 5, 1 is 6 and so on)
    * we have, simply, splayed the circle. travelleing from index zero to 5 is the same as travelling the circle; case applies for 1 to 6, 2 to 7, 3 to 8 and 4 to 9
* set `start` to zero. empty tank. fill with `petrol` amount and use `cost` amount to get to the next index. `curr` tracks how much fuel is left in our tank. `start` is used to traverse the arrays
    * is `curr` less than 0?
        * yes
            * set `curr` to zero
            * set `start` to i + 1
        * no: continue
    * is `i` == `start` + N?
        * yes
            * return `start`
        * no
            * continue

### code
* see [9-petrol_station.py][def]

[def]: ./9-petrol_station.py