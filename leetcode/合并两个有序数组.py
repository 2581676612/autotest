"""
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。
"""

import time


class Solution:
    def merge(self, nums1, m, nums2, n):
        total = m + n
        for i in range(m, total):
            nums1[i] = nums2[total - i - 1]
        nums1.sort()

    def merge_1(self, nums1, m, nums2, n):
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            for i in range(n):
                length = m + i
                while length > 0:
                    length -= 1
                    if nums2[i] >= nums1[length]:
                        nums1[length+1] = nums2[i]
                        break
                    else:
                        nums1[length], nums1[length + 1] = nums2[i], nums1[length]


if __name__ == '__main__':
    nums1 = [0]
    nums2 = [1]
    m, n = 0, 1
    s = Solution()
    s.merge_1(nums1, m, nums2, n)
