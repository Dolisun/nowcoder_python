# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        #思路：冒泡法每次从左往右走一趟会把最大的数放大最后，那么我们可以从右往左走一趟把最小的数字放最左边，走k趟就行了
        length = len(tinput)
        if length < k or k < 0:
            return []
        for i in range(k):
            for j in range(length-1, i, -1):
                if tinput[j] < tinput[j-1]:
                    tinput[j],tinput[j-1] = tinput[j-1],tinput[j]
        return tinput[0:k]
