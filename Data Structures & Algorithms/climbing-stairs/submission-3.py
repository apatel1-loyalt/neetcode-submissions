class Solution:
    def climbStairs(self, n: int) -> int:
        f1, f2  = 0, 1

        for i in range(n+1):
            tmp = f1
            f1 = f1 + f2 
            f2 = tmp 

        return f1