class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count, rotten_fruit = self.fruitCount(grid)

        # if there are no fresh fruit 
        if fresh_count == 0:
            return 0

        # if there are no rotten fruit
        if not rotten_fruit:
            return -1


        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        time = 0

        while rotten_fruit and fresh_count != 0:

            # We do one level at a time
            level = len(rotten_fruit)

            for _ in range(level):

                r, c = rotten_fruit.popleft()

                for dr, dc in direction:

                    nr, nc = r+dr, c+dc
                    
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten_fruit.append((nr, nc))
                        fresh_count -= 1

            time += 1
            
        
        return -1 if fresh_count != 0 else time 



    def fruitCount(self, grid):
        """Count Rotten and Fesh Fruits And also rotten fruits cordinates"""

        rotten_fruit = deque()
        fresh_fruit_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_fruit_count += 1
                elif grid[i][j] == 2:
                    rotten_fruit.append((i, j))
                else:
                    continue

        return fresh_fruit_count, rotten_fruit