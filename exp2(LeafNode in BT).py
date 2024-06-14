class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def printLeafNodes(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.val)
        return
    if node.left:
        printLeafNodes(node.left)
    if node.right:
        printLeafNodes(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

printLeafNodes(root)