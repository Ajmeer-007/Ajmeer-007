class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,val in enumerate(nums):
            com = target-val
            if com in seen:
                return ([seen[com],i])
                break
            seen[val] = i
