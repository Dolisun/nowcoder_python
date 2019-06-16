# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        list = []
        if len(ss) <= 1:
            return ss
        for i in range(len(ss)):
            for j in map(lambda x: ss[i]+x, self.Permutation(ss[:i]+ss[i+1:])):
                # print(j)
                # print('\n', list)
                if j not in list:
                    list.append(j)
        return list


so = Solution()
print(so.Permutation('abc'))
