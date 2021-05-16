"""
给定一个非空且只包含非负数的整数数组nums，数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是在 nums 中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。
输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
"""

import collections
class Solution:
    def findShortestSubArray(self, nums):
        short_len = len(nums)
        left_dict, right_dict = {}, {}
        for i, num in enumerate(nums):
            if num not in left_dict:
                left_dict[num] = i
            right_dict[num] = i
        count_model = collections.Counter(nums)
        du = max(collections.Counter(nums).values())
        for k, v in count_model.items():
            if v == du:
                short_list = nums[left_dict[k]: right_dict[k]+1]
                short_len = min(short_len, len(short_list))
        print(short_len)
        return short_len


if __name__ == '__main__':
    s = Solution()
    s.findShortestSubArray([1,2,2,3,1])
