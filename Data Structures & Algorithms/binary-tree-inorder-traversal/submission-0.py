# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        ans = self.travel(root, ans)

        return ans if ans else []

    def travel(self, root, ans):

        # Return if end is found
        if not root:
            return
        
        # Go Left first
        self.travel(root.left, ans)

        ans.append(root.val)

        # Go right after left
        self.travel(root.right, ans)

        return ans
