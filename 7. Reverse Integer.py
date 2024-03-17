class Solution(object):
    def reverse(self, x):
        sign = 1 # if x is positive "+"

        if x == 0:
            return 0
        elif x < 0: # if x is negative "-"
            sign = -1
            x = abs(x)

        # Converting integer to string, reversing it, and converting it back to integer
        reversed_x = int(str(x)[::-1]) * sign

        # Check if reversed integer is within the 32-bit signed integer range
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0

        return reversed_x
