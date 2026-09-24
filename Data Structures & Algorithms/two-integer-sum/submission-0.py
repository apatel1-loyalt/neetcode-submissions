class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            number = nums[i]
            rem = target - number

            if rem not in count:
                if number not in count:
                    count[number] = i
            else:
                
                return[min(i, count[rem]), max(i, count[rem])]