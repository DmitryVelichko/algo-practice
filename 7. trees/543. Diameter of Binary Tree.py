# 543. Diameter of Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS() returns h, update maxDiameter (left subtree height + right subtree height)
# T: O(n), S: O(h) - O(log n) for balanced tree, O(n) for unbalanced
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # function returns the height, not diameter
        def dfs(root):
            nonlocal res
            if not root: return 0

            left = dfs(root.left) # h of left subtree
            right = dfs(root.right) # h of right subtree
            res = max(res, left + right) # left + right = diameter of a tree

            return 1 + max(left, right)

        dfs(root)
        return res