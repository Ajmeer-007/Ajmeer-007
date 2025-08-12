class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close  = nums[0]
        for i in nums:
            if abs(i)<abs(close):
                close = i

        if abs(close) in nums:
            return abs(close)

        else:
            return close
