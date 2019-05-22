# -*- coding:utf-8 -*-
# class Solution:
#     # s 源字符串
#     def replaceSpace(self, s):
#         # write code here
#         L = len(s) - 1
#         p = 0
#         while p <= L:
#             if s[p] == ' ':
#                 if p == L:
#                     s = s[:p] + '%20'
#                     p += 1
#                 else:
#                     s = s[:p] + '%20' + s[p+1:]
#                     p += 1
#             p += 1
#         return s
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #return s.replace(' ','%20')
        s = list(s)
        a = len(s)
        for i in range(a):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)

so = Solution()
print(so.replaceSpace(" "))
