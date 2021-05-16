class Solution:
    def isMonotonic(self, A):
        dandiao_A = sorted(A)
        if A == dandiao_A:
            return True
        dandiao_A.reverse()
        if A == dandiao_A:
            return True
        return False

    def isMonotonic_1(self, A):
        if self.more_than(A) or self.less_than(A):
            return True
        return False

    def more_than(self, A):
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True

    def less_than(self, A):
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                return False
        return True

A = [6,5,6,4]
S = Solution()
print(S.isMonotonic_1(A))