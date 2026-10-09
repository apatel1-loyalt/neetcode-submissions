class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        visited = set()

        r, c = 0, 0

        while r < len(grid):
            c = 0 
            while c < len(grid[0]):
                island_count += self.isIsland(r, c, visited, grid)
                c += 1
            r += 1

        return island_count

    def isIsland(self, r, c, visited, grid):

        ROW, COL = len(grid), len(grid[0])

        if min(r, c) < 0 or r >= ROW or c >= COL or grid[r][c] == '0' or (r, c) in visited:
            return 0

        visited.add((r, c))

        self.isIsland(r + 1, c, visited, grid)
        self.isIsland(r - 1, c, visited, grid)
        self.isIsland(r, c + 1, visited, grid)
        self.isIsland(r, c - 1, visited, grid)

        return 1
