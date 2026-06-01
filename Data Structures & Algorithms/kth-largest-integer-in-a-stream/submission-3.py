# Sorted Array Method

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.nums = k, nums
        
    def add(self, val: int) -> int:
        # Add the new member to the list
        self.nums.append(val)
        self.nums.sort()

        return self.nums[-self.k]
        
