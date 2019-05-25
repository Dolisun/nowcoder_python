# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        head = ListNode(-1)
        p3 = head
        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            else:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
        if p1:
            p3.next = p1
        if p2:
            p3.next = p2
        return head.next