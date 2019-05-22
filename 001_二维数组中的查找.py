# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0
        j = len(array[0]) - 1
        L = len(array) - 1
        while (j >= 0) & (i <= L):
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
# 本地测试
so = Solution()
print(so.Find(5,[[1,2,3],[2,3,4]]))

