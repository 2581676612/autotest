from collections import Counter


class Solution:
    def longestSubstring(self, s, k):
        max_len = 0
        s_list = self.get_all_str(s)
        for i in s_list:
            max_len = max(max_len, self.get_all_count(i, k))
        print(max_len)
        return max_len

    def get_all_str(self, s):
        s_len = len(s)
        s_list = [s[i:j + 1] for i in range(s_len) for j in range(i, s_len)]
        return s_list

    def get_all_count(self, l, k):
        c = Counter(l)
        if not c:
            return 0
        min_val = min(c.values())
        if c and min_val >= k:
            print(l)
            return sum(c.values())
        return 0


st = "ababacb"
s = Solution()
s.longestSubstring(st, 2)
