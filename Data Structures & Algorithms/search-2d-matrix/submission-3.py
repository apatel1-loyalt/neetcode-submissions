class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We merge the arrays and find the target using binary search 
        lst = []
        for x in matrix:
            lst += x

        # Search Range
        l, r, m = 0, len(lst) - 1, 0

        # Looping until l or r cross over eachother or out or range
        while l <= r:

            m = (l + r) // 2

            if lst[m] < target:
                l = m + 1
            elif lst[m] > target:
                r = m - 1
            else:
                return True
        
        return False

    