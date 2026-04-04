class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # We create a array of 2 times length of nums
        ans = [0] * (2 * len(nums))

        # loop the array 
        for i in range(len(nums)):

            # Set the first and n+first as nums[i]
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        
        return ans