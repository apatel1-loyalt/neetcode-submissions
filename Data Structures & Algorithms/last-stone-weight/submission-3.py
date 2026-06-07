class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Brute Force Method

        i = len(stones) - 1

        while (i > 0):
            # Sort the array 
            stones.sort()

            # We go to last one and one before
            # Find the diff and save it to before_last
            stones[i-1] = abs(stones[i] - stones[i-1])

            # Moving condition 
            i -= 1
        
        # Return the first member 
        return stones[0]