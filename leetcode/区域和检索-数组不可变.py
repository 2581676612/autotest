"""
给定一个整数数组 nums，求出数组从索引i到j（i≤j）范围内元素的总和，包含i、j两点。
实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引i到j（i≤j）范围内元素的总和，包含i、j两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
例：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
"""


class NumArray:

    def __init__(self, nums):
        self.pre_sum = [0]
        for i in range(len(nums)):
            self.pre_sum.append(sum(nums[:i+1]))
        print(self.pre_sum)

    def sumRange(self, i, j):
        return self.pre_sum[j+1]-self.pre_sum[i]


l = [-2, 0, 3, -5, 2, -1]
n = NumArray(l)
n.sumRange(0, 2)
