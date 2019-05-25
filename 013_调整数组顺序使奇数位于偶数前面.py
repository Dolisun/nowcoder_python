# -*- coding:utf-8 -*-
# 思路是先找到第一偶数，然后从这个偶数开始往后找奇数，遇到奇数就把这个奇数移到第一个偶数后面
class Solution:
    def reOrderArray(self, array):
        # write code here
        p1 = 0
        # 找到第一个偶数
        while p1 < len(array):
            if array[p1] % 2 == 0:
                break
            else:
                p1 += 1
        p2 = p1 + 1
        while p2 < len(array):
            if array[p2] % 2 == 1:
                tmp = array[p2]
                array[p1+1:p2+1] = array[p1:p2]
                array[p1] = tmp
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return array