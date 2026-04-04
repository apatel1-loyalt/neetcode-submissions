class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We use binary search on the lists and see which list might contain the target 
        # then we use binary search again to find the target inside

        row_index = 0 

        for row in matrix:
            if row[-1] >= target and row[0] <= target:
                break
            
            row_index += 1

        if len(matrix) <= row_index:
                return False

        # now in the list find the target
        
        # Search Range
        row = matrix[row_index]
        l, r, m = 0, len(row) - 1, 0

        # looping until l and r are out of bound for our search range
        while l <= r:
            m = (l + r) // 2
            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True

        return False
        