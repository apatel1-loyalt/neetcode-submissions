class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """Using BFS"""
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] == 0:
                        queue.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
            length += 1
    
        return -1