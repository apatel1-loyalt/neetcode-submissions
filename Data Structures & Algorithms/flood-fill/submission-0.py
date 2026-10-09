class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        return self.fill(image, sr, sc, image[sr][sc], color)
        

    def fill(self, image, sr, sc, starting_pixel, color):

        ROW, COL = len(image), len(image[0])

        # Breaking Condition
        if min(sr, sc) < 0 or sr == ROW or sc == COL or image[sr][sc] == color or image[sr][sc] != starting_pixel:
            return

        # original logic
        image[sr][sc] = color

        # Moving to all other pixels
        self.fill(image, sr+1, sc, starting_pixel, color)
        self.fill(image, sr-1, sc, starting_pixel, color)
        self.fill(image, sr, sc+1, starting_pixel, color)
        self.fill(image, sr, sc-1, starting_pixel, color)

        # Return the Original Image
        return image