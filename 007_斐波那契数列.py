# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        f0, f1= 0, 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n+1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2