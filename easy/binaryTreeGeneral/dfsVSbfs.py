# TreeNode definition
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# DFS using recursion
def dfs(root):
    if root is None:
        return
    
    # Process the current node (preorder traversal)
    print(root.value)
    
    # Recursively visit the left subtree
    dfs(root.left)
    
    # Recursively visit the right subtree
    dfs(root.right)

# Example usage
root = TreeNode(1, TreeNode(2), TreeNode(3))
dfs(root)

# ___________________________________________________________

from collections import deque

# BFS using a queue
def bfs(root):
    if root is None:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        
        # Process the current node
        print(node.value)
        
        # Enqueue left child
        if node.left:
            queue.append(node.left)
        
        # Enqueue right child
        if node.right:
            queue.append(node.right)

# Example usage
root = TreeNode(1, TreeNode(2), TreeNode(3))
bfs(root)
