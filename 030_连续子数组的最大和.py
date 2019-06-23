# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        # 思路：不停累加，当前面累加的结果为负时，将结果置零，从这个地方重新开始
        res = []
        tmp = 0
        for i in array:
            tmp += i
            res.append(tmp)
            if tmp < 0:
                tmp = 0
        return max(res)