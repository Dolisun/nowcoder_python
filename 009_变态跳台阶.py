# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        f1 = 1
        for i in range(2, number+1):
            f2 = 2 * f1
            f1 = f2
        return f2