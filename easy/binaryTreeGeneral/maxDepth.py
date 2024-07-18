def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # finding max DEPTH --> so this is DFS
    #           3
    #        9     20
    #            15   7

    # base case 
    if root == None: return 0

    # find max depth on both sides
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    return 1 + max(left_depth, right_depth)
