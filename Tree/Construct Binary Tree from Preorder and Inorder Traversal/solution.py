# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        stack = deque()
        i = 0
        flag = True
        cur = None

        for node in preorder:
            while stack and stack[-1].val == inorder[i]:
                cur = stack.pop()
                flag = False
                i += 1

            new_node = TreeNode(node)
            stack.append(new_node)

            if cur:
                if not cur.left and flag:
                    cur.left = new_node
                else:
                    cur.right = new_node
            else:
                root = new_node
            cur = new_node
            flag = True

        return root
