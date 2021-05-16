"""
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
"""


class Solution1:
    def search_1(self, nums, target):
        return target in nums

    def search(self, nums, target):
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (right + left) // 2
            print(left, right, mid)
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid]:
                left += 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


class Solution:
    def search(self, nums, target):
        if not nums:
            return False
        lens = len(nums)
        left, right = 0, lens - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid]:
                left += 1
            elif nums[left] < nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        if nums[left] == target:
            return True
        else:
            return False


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
    target = 2
    s = Solution()
    print(s.search(nums, target))
