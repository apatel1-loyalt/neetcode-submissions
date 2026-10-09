class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        if color == starting_pixel:
            return image   

        ROW, COL = len(image), len(image[0])

        def fill(r, c):

            # Breaking Condition
            if min(r, c) < 0 or r == ROW or c == COL or image[r][c] == color or image[r][c] != starting_pixel:
                return

            # original logic
            image[r][c] = color

            # Moving to all other pixels
            fill(r+1, c)
            fill(r-1, c)
            fill(r, c+1)
            fill(r, c-1)

        fill(sr, sc)
        # Return the Original Image
        return image