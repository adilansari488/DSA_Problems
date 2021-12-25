"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123 Output: 321

Example 2:

Input: x = -123 Output: -321

Example 3:

Input: x = 120 Output: 21

Constraints:

-2^31 <= x <= 2^31 - 1
"""

#SOLUTION

def reverse(x) :
    ans = 0
    if x == 0 :
        return 0                       # if x==0 return 0
    elif x > 0 :                       # if x greater than 0
        while x != 0 :                 # loop 
            digit = x%10               # calculate value at unit position
            if ans > (2**31 - 1)/10 :  # max range of 32 bit int
                return 0               # return 0
            ans = (ans*10) + digit     # calculate ans.
            x = x//10
        return ans                     # return vlaue
    else :                             # Same process for negative value
        x = -x                         # Converting negative input to ppositive
        while x != 0 :                 # same overall calculateion
            digit = x%10
            if ans > (2**31)/10 :
                return 0
            ans = (ans*10) + digit
            x = x//10
        return -ans                   # Converting positive ans to negative because input was negative
