class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # using Binary Search 

        # Search Range
        l, r, m = 0, len(nums) - 1, 0

        # looping until l or r gets out of bound
        while l <= r:

            # Finding middle
            m = (l + r) // 2

            # Comparing with the target
            if (target > nums[m]):
                # We go right
                l = m + 1
            elif (target < nums[m]):
                # We go left
                r = m - 1
            else:
                # We find the target
                return m

        # if we dont find 
        return -1