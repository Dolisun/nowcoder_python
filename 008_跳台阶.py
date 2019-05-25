# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        f1, f2 = 1, 2
        for i in range(3, number+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3