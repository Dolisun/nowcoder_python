# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or not k:
            return None
        p2 = head
        # 先找到第k个位置的节点
        for i in range(k-1):
            if not p2.next:
                return None
            p2 = p2.next
        p1 = head
        # 保持k的距离，两个指针同时移动，当后面那个移动到头前面那个就是倒数第k个了
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        return p1