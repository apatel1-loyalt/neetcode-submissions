class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using Bubble Sorting 

        # Counting all the colours
        counts = [0, 0, 0]
        for i in range(len(nums)):
            counts[nums[i]] += 1

        # Using Count to Update the array
        i = 0
        for j in range(len(counts)):
            for n in range(counts[j]):
                nums[i] = j
                i += 1