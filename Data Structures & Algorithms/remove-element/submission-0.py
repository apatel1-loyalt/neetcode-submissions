class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Using Two Pointer Algorithum
        write_pointer = 0 # left pointer
        read_pointer = 0 # right pointer

        # loop the list 
        while read_pointer < len(nums):

            # Check if the current read pointer member matches the val
            if val != nums[read_pointer]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

            # moving condition 
            read_pointer += 1

        return write_pointer