# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        store = dict()
        return self.get_tree_nodes(1, n, store)

    def get_tree_nodes(self, start, end, store):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        tree_list = []
        for root in range(start, end + 1):
            left_nodes = []
            right_nodes = []
            if (start, root - 1) in store:
                left_nodes = store[(start, root - 1)]
            else:
                left_nodes = self.get_tree_nodes(start, root - 1, store)
                store[(start, root - 1)] = left_nodes

            if (root + 1, end) in store:
                right_nodes = store[(root + 1, end)]
            else:
                right_nodes = self.get_tree_nodes(root + 1, end, store)
                store[(root + 1, end)] = right_nodes
            for left_node in left_nodes:
                for right_node in right_nodes:
                    new_tree = TreeNode(root, left_node, right_node)
                    tree_list.append(new_tree)
        return tree_list
