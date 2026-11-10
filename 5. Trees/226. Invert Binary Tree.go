package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// DFS recursive pre-order: Time: O(n), Space: O(h), h = height (maximum depth) of the tree
// Balanced tree: O(log n), Skewed tree (linked list): O(n)

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	root.Left, root.Right = root.Right, root.Left
	invertTree(root.Left)
	invertTree(root.Right)
	return root
}

// DFS iterative with stack

func invertTreeIterative(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	stack := []*TreeNode{root}

	for len(stack) > 0 {
		// Pop the top of the stack
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		// Swap children nodes
		node.Left, node.Right = node.Right, node.Left

		// Push non-nil children to the stack
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}

	return root
}
