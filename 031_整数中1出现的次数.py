# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        # 思路：https://www.cnblogs.com/nailperry/p/4752987.html
        a = 1
        num = 0
        while n // a:
            div, mod = divmod(n, a * 10)
            cur, low = divmod(mod, a)
            if cur > 1:
                num += (div + 1) * a
            elif cur == 1:
                num += div * a + low + 1
            else:
                num += div * a
            a = a * 10
        return num