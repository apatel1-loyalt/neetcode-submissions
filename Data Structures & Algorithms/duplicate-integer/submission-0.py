class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                return True

        return False