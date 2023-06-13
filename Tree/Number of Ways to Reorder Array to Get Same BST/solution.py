class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        root = self.bst(nums)
        return self.dfs(root)[0] - 1

    def bst(self, nums):
        root = Node(nums[0])
        for num in nums:
            self.traverse(root, num)
        return root

    def traverse(self, node, num):
        if num == node.val:
            return
        if num > node.val:
            if node.right:
                self.traverse(node.right, num)
            else:
                node.right = Node(num)
        else:
            if node.left:
                self.traverse(node.left, num)
            else:
                node.left = Node(num)
        

    def dfs(self, node):
        left, right = 1, 1
        total_left, total_right = 0, 0
        if node.left:
            left, total_left = self.dfs(node.left)
        if node.right:
            right, total_right = self.dfs(node.right)
        total = total_left + total_right + 1
        combination = (self.combine(total_left, total_right) * left * right) % (10 ** 9 + 7)
        return combination, total
    
    def combine(self, a, b):
        top, down = 1, 1
        for i in range(1, b + 1):
            top *= (a + i)
            down *= i
        return top // down