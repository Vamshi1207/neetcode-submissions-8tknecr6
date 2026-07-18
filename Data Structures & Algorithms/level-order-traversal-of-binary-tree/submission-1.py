# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levelsMap = {}

        if not root:
            return []
        level = 0        
        
        def getNodeLevels(root, levelsMap, level):
            level += 1

            levelsMap.setdefault(level, []).append(root.val)

            if root.left:
                getNodeLevels(root.left, levelsMap, level)
            if root.right:
                getNodeLevels(root.right, levelsMap, level)
        
        getNodeLevels(root, levelsMap, level)

        return list(levelsMap.values())
