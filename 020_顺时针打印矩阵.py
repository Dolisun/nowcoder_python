# -*- coding:utf-8 -*-
# 先逆时针旋转90度，再取第一行
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        flag = 0
        while matrix:
            matrix = self.rotate(matrix, flag)
            flag += 1
            res.extend(matrix.pop(0))
        return res

    def rotate(self, m, flag):
        if flag == 0:
            return m
        dim1 = len(m)
        dim2 = len(m[0])
        m1 = []
        for j in range(dim2-1, -1, -1):
            new = []
            for i in range(dim1):
                new.append(m[i][j])
            m1.append(new)
        return m1
