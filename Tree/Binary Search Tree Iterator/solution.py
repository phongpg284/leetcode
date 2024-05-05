# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.orders = []
        self.in_order_traverse(root)
        self.index = -1
        self.length = len(self.orders)

    def in_order_traverse(self, node):
        if node.left:
            self.in_order_traverse(node.left)

        self.orders.append(node.val)

        if node.right:
            self.in_order_traverse(node.right)

    def next(self) -> int:
        self.index += 1
        return self.orders[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
