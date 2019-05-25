# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        low = 0
        high = len(rotateArray) - 1
        while rotateArray[low] >= rotateArray[high]:
            if high - low == 1:
                mid = high
                break
            mid = (low + high) // 2
            if (rotateArray[low] == rotateArray[mid]) & (rotateArray[high] == rotateArray[mid]):
                min(rotateArray)
            elif rotateArray[mid] >= rotateArray[low]:
                low = mid
            elif rotateArray[mid] <= rotateArray[high]:
                high = mid
        return rotateArray[mid]


so = Solution()
print(so.minNumberInRotateArray([1,0,1,1,1,1]))