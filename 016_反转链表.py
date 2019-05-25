# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        if not pHead.next:
            return pHead
        p1 = pHead
        p2 = p1.next
        p1.next = None
        while p2.next:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        p2.next = p1
        return p2