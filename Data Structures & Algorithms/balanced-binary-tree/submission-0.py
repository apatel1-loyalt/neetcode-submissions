# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        def inner(root):
            if not root: return [0, True]

            left, right = inner(root.left), inner(root.right)

            balanced = abs(left[0]-right[0]) <= 1 and left[1] and right[1]

            return [1 + max(left[0], right[0]), balanced]

        return inner(root)[1]