# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        f = 1
        if exponent == 0:
            return 1
        elif exponent > 0:
            for i in range(exponent):
                f = f * base
        else:
            for i in range(-exponent):
                f = f * base
            f = 1 / f
        return f