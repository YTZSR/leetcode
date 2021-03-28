# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.list = treeTolist(root)

    def treeTolist(root: TreeNode):
        if root is None:
            return []
        else:
            return treeTolist(root.left).append(root.val).append(root.right)

    def next(self) -> int:
        return self.list.pop(0)

    def hasNext(self) -> bool:
        return len(self.list) == 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()