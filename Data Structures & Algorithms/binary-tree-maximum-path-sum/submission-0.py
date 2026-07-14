# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')
        
        def get_max_gain(node):
            if not node:
                return 0
            
            # 1. Recursively get the max path sum from left and right subtrees.
            # 2. If a path sum is negative, we drop it by taking max(..., 0).
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # 3. Price of the "Arch" (path passes through this node and both children)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum if this "Arch" is the best we've seen
            self.global_max = max(self.global_max, current_path_sum)
            
            # 4. Return the max "Straight Line" path sum this node can contribute to its parent
            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        return self.global_max