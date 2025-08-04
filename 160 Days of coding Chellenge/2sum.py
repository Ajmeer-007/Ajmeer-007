class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(nums):
            com = target-j
            if com in seen:
                return ([seen[com],i])
            seen[j]=i
