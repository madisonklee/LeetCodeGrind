def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p is None and q is None:     # identical --> return True
        return True
    if p is None or q is None:      # not identical --> False
        return False
    if p.val == q.val:              # recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    # values are not equal, they are not identical
    return False