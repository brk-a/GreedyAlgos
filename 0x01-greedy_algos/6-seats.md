# seats

### the problem
there is a row of empty seats, (.), and filled ones, (x)

find the minimum #moves required to place the filled seats
together

constraint
*  1 <= N <= 1e6

### test cases
* "..x..x."
    * N = 7
    * output: 2
    * either filled seat makes two moves
        * "....xx."
        * "..xx..."
* ".x..x..xx."
    * N = 9
    * output: 6
    * there are may configurations; the least cost one has a cost
    of 6
> > **observation: algo takes O(N²) time**
* "xx..xx....xxxx"
    * N = 13
    * output 5
> > **pattern: find the median of the indices of the occupied seats**
### complexity
* O(N) when you eliminate an unnecessary iterations

### optimisation
* find the median of the indices of the occupied seats
* cluster all the points around the median

### code
* see [6-seats.py][def]

[def]: ./6-seats.py