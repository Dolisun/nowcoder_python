# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        compare = lambda a, b:cmp(str(a) + str(b), str(b) + str(a))
        min_string = sorted(numbers, cmp = compare)
        return ''.join(str(s) for s in min_string)