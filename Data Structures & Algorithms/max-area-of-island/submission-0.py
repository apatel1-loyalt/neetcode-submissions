class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, area = 0, 0

        ROW, COL = len(grid) , len(grid[0])

        def calArea(r, c, area):

            if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 1

            area += calArea(r+1, c, area)
            area += calArea(r-1, c, area)
            area += calArea(r, c+1, area)
            area += calArea(r, c-1, area)

            return area
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = calArea(r, c, 0)
                    max_area = max(area, max_area)

        return max_area
        