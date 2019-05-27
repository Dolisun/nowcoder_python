# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        tmp = sequence.pop()
        left = []
        right = []
        # 最后一个数为根结点，根结点左子树都小于根结点，右子树都大于
        while sequence and sequence[0] < tmp:
            left.append(sequence.pop(0))
        while sequence and sequence[0] > tmp:
            right.append(sequence.pop(0))
        # 如果左右分开之后，原始序列里面还有数，表明原始序列没有按照左边小，右边大的规则
        if sequence:
            return False
        # 如果出现空的情况，就不用继续递归了
        if len(left) > 0 and len(right) > 0:
            res = self.VerifySquenceOfBST(left) and self.VerifySquenceOfBST(right)
        elif len(left) == 0:
            res = self.VerifySquenceOfBST(right)
        else:
            res = self.VerifySquenceOfBST(left)
        return res