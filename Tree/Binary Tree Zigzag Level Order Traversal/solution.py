# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        store = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if level % 2 == 0:
                store[level].append(node.val)
            else:
                store[level].insert(0, node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return store.values()
