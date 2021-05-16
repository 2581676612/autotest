"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
"""


class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i+2]:
                nums.remove(nums[i+2])
                continue
            i += 1
        return len(nums)


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    s = Solution()
    print(s.removeDuplicates(nums))
