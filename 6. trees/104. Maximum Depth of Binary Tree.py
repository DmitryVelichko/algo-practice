# 104. Maximum Depth of Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#DFS recursive O(n), O(h): which is O(n) in worst case of an unbalanced tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
#DFS iterarive O(n), O(h): which is O(n) in worst case of an unbalanced tree
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxDepth = 1
        stack = [[root,1]]
        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left: stack.append([node.left, depth+1])
            if node.right: stack.append([node.right, depth+1])
        return maxDepth
#BFS  O(n), O(w), w is width of the tree, worst case: O(n) coz in a balanced binary tree the bottom layer contains roughly half of all nodes n/2. BFS tracks nodes layer by layer. 
# node, depth = queue.pop(0)
     
  