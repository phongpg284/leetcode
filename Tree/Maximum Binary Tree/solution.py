# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        max_val = -1
        max_idx = -1

        for i, num in enumerate(nums):
            if num > max_val:
                max_val = num
                max_idx = i

        left = self.constructMaximumBinaryTree(nums[:max_idx])
        right = self.constructMaximumBinaryTree(nums[max_idx + 1:])

        root = TreeNode(max_val, left, right)

        return root
