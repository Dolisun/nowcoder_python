# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 基本思路是 先比较根结点，如果根节点相同，那么比较左右子树，就是一个递归过程了。如果根结点不相等，那么用左子树或者右子树做比较
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.isSubtree(pRoot1, pRoot2)

    def isSubtree(self, p1, p2):
        if not p2:
            return True
        if not p1:
            return False
        res = False
        if p1.val == p2.val:
            res = self.isSubtree(p1.left, p2.left) and self.isSubtree(p1.right, p2.right)
        return res or self.isSubtree(p1.left, p2) or self.isSubtree(p1.right, p2)