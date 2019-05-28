# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        p = pHead
        #将每个节点复制一份放在该节点的后一个节点，这样每个节点的随机指针的下一个节点就是
        #这个这个节点的备份节点的随机指针
        while p:
            new = RandomListNode(p.label)
            new.next = p.next
            p.next = new
            p = new.next
        # 寻找节点的随机节点
        p = pHead
        while p:
            p1 = p.next
            if p.random:
                p1.random = p.random.next
            p = p1.next
            
        head = pHead.next
        p1 = head
        p = pHead
        while p:
            p.next = p.next.next
            if p1.next:
                p1.next = p1.next.next
            p1 = p1.next
            p = p.next
        return head