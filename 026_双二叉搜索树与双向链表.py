# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.head=None
        self.p = None
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.Convert(pRootOfTree.left)
        if not self.head:
            self.head = pRootOfTree
            self.p = pRootOfTree
        else:
            self.p.right = pRootOfTree
            pRootOfTree.left = self.p
            self.p = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.head