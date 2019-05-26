# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return True if not stack else False