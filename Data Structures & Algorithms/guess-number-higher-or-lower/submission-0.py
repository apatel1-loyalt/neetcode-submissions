# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # Binary Search

        # Seach Area is from 1 -> n
        low = 1 
        high = n

        # Now we loop till we find the number or low or high becomes out of bound 
        while low <= high:

            # finding the middle point
            m = (low + high) // 2

            # conditions for checking 
            g = guess(m)

            if g == 1:
                low = m + 1
            elif g == -1 :
                high = m - 1
            else:
                return m

        