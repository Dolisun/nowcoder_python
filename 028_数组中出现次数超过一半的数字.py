# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        dict = {}
        for i in numbers:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
            if dict[i] > len(numbers) // 2:
                return i
        return 0