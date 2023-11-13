# meeting rooms

### the problem
there is an array of an array of two ints, s 
and e. said ints represent the start and end,
inclusive, of a meeting

find the least number of meeting rooms required

constraints:
* 1 <= N <= 1e5 (N is the number of meetings)
* 1 <= A[i][0] <= A[i][1] <= 1e9 (a meeting can end at 1e9)

### test cases
* [[5, 10], [15, 20], [0, 30]]
    * output is 2
    * [0, 30] and [15, 20] take place simultaneously;
    same for [0, 30] and [5, 10]
    * [0, 30] and [15, 20] overlap; [0, 30] and
    [5, 10] as well. [5, 10] and [15, 20] do not

### complexity

### optimisation
* we only care about the overlaps, therefore, focus on the elements of each sub-array
    * add 1 for each element on the left (s)
    * subtract 1 for each element on the right (e)

    |start|add op|end|less op|
    |:---|:---:|:---:|:---:|
    |5|+1|10|-1|
    |15|+1|20|-1|
    |0|+1|30|-1|

    * create a list of tuples and sort it

    ```python
        [
            (0, 1),
            (5, 1),
            (10, -1),
            (15, 1),
            (20, -1),
            (30, -1),
        ]
    ```

    * at zero, `curr` is set to 1 (there is one meeting in progress); `_max`
    is set to 1 (we need one meeting room, so far)
    * at 5, *curr* is set to 2; so is *_max*
    * at 10 *curr* is set to 1 (2 + -1); *_max* remains 2
    * at 15 *curr* is set to 2; *_max* remains two because only two meetings
    are simultaneously in progress
    * at 20 *curr* is set to 1; *_max* remains 2
    * at 30 *curr* is set to zero (all meetings have ended); *_max* remains 2 
    * return *_max*; we needed two meeting rooms at a time max
*

### code
* see [4-meeting_rooms.py][def]
* create a list of tuples and sort it
* initialise `curr` and `_max`
* iterate over the sorted array
    * add the rightmost value of each tuple to *curr*
    * set *_max* to the maximum of *_max* and *curr* as at that iteration
* return *_max*

[def]: ./4-meeting_rooms.py