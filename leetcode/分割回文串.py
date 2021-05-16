"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数。
"""


class Solution:
    def minCut(self, s):
        s_list = self.get_all_str(s)
        min_count = 999
        for s_l in s_list:
            if self.is_huiwen(s_l):
                pass

    def get_all_str(self, s):
        s_len = len(s)
        s_list = [s[i:j + 1] for i in range(s_len) for j in range(i, s_len)]
        print(s_list)
        return s_list

    def is_huiwen(self, s):
        l = len(s)
        for i in range(l//2):
            if s[i] != s[l-i-1]:
                return False
        return True



st = "aabcaa"
s = Solution()
# s.minCut(st)
print(s.is_huiwen(st))