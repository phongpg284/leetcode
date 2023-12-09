/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func inorderTraversal(root *TreeNode) []int {
	res := []int{}
	var inOrder func(root *TreeNode)
	inOrder = func(node *TreeNode) {
		if node != nil {
			inOrder(node.Left)
			res = append(res, node.Val)
			inOrder(node.Right)
		}
	}
	inOrder(root)
	return res
}
 