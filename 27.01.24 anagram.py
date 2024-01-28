Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.
Input Format

The first line will contain an integer, , the number of test cases.
Each test case will contain a string .

Constraints


 consists only of characters in the range ascii[a-z].
Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
Sample Output

3
1
-1
2
0
1
Explanation

Test Case #01: We split  into two strings ='aaa' and ='bbb'. We have to replace all three characters from the first string with 'b' to make the strings anagrams.

Test Case #02: You have to replace 'a' with 'b', which will generate "bb".

Test Case #03: It is not possible for two strings of unequal length to be anagrams of one another.

Test Case #04: We have to replace both the characters of first string ("mn") to make it an anagram of the other one.

Test Case #05:  and  are already anagrams of one another.

Test Case #06: Here S1 = "xaxb" and S2 = "bbxx". You must replace 'a' from S1 with 'b' so that S1 = "xbxb".

Submissions: 48
Max Score: 25
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
​
9
#
10
# Complete the 'anagram' function below.
11
#
12
# The function is expected to return an INTEGER.
13
# The function accepts STRING s as parameter.
14
#
15
​
16
def anagram(s):
17
    # Write your code here
18
    strlen = len(s)
19
    if strlen == 0 or strlen%2 != 0:
20
        return -1
21
​
22
    tochange = 0
23
    sublen = strlen//2
24
    lhs, rhs = s[:sublen], list(s[sublen:])
25
    for char in lhs:
26
        if char not in rhs:
27
            tochange += 1
28
        else:
29
            rhs.remove(char)
30
    return tochange
31
​
32
if __name__ == '__main__':
33
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
34
​
35
    q = int(input().strip())
36
​
37
    for q_itr in range(q):
38
        s = input()
39
​
40
        result = anagram(s)
41
​
42
        fptr.write(str(result) + '\n')
43
​
44
    fptr.close()
45
​
