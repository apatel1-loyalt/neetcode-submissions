class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """BiDirection Matrix BFS"""

        # Edge Condition
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROW, COL = len(grid), len(grid[0])
        if ROW == 1:
            return  1

        length = 2

        visited = set()

        option1 = deque([(0, 0)])
        option2 = deque([(ROW - 1, COL - 1)])

        start, end = -1, -2

        grid[0][0], grid[-1][-1] = start, end

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while option1 and option2:
            for _ in range(len(option1)):
                row, col = option1.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < ROW and 0 <= nc < COL:
                        if grid[nr][nc] == end:
                            return length

                        if grid[nr][nc] == 0 and (nr, nc) not in visited:
                            grid[nr][nc] = start
                            visited.add((nr, nc))
                            option1.append((nr, nc))

            # Swap the options so we move from both side
            option1, option2 = option2, option1
            start, end = end, start
            length += 1

        return -1
