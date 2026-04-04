class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       # Editing the same array

       # Looping the input array 
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums