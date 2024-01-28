Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
Submissions: 70
Max Score: 15
Difficulty: Easy
Rate This Challenge:

    
More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
from datetime import datetime
9
​
10
#
11
# Complete the 'timeConversion' function below.
12
#
13
# The function is expected to return a STRING.
14
# The function accepts STRING s as parameter.
15
#
16
​
17
def timeConversion(s):
18
    time_12hr = datetime.strptime(s, '%I:%M:%S%p')
19
    
20
    time_24hr = time_12hr.strftime('%H:%M:%S')
21
    
22
    return time_24hr
23
​
24
if __name__ == '__main__':
25
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
26
​
27
    s = input()
28
​
29
    result = timeConversion(s)
30
​
31
    fptr.write(result + '\n')
32
​
33
    fptr.close()
Line