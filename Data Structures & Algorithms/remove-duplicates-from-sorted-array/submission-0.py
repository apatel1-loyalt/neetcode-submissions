class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       # Using Two Pointer
        reading_pointer = 1 # Right pointer
        writing_pointer = 0 # Left pointer

        # looping the list
        while reading_pointer < len(nums):
            
            # Compare the current and previous member from reading pointer
            if (nums[reading_pointer] != nums[reading_pointer-1]):
                nums[writing_pointer] = nums[reading_pointer-1]
                writing_pointer += 1

            # Moving condition
            reading_pointer += 1
        
        nums[writing_pointer] = nums[reading_pointer-1] 

        return writing_pointer + 1