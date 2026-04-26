# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """ Using BackTracking Algorithum Here"""

        # Breaking Condition for the recursive call
        if not root: 
            return False

        # New target Sum
        targetSum -= root.val

        # Now check if we already have the targetsum or not
        if not root.right and not root.left and targetSum == 0:
            return True

        # Go left
        if self.hasPathSum(root.left, targetSum):
            return True
        
        # Go Right
        if self.hasPathSum(root.right, targetSum):
            return True

        # Add the removed value if this is not correct path
        targetSum += root.val

        # If no solution found
        return False
        