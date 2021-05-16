class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n_length = len(needle)
        for i in range(len(haystack) - n_length + 1):
            if haystack[i:i + n_length] == needle:
                return i
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('123', '3'))
