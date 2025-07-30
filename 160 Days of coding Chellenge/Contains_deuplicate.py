class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:# Both T&S are O(n)
        a = set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False


#another methon o(n)T &O(1)S

    def hasDuplicate(self,nums):
        for i in range(len(nums):
            index = abs(nums[i])-1
            if nums[index]<0:
                return True
            nums[index]= -nums[index]
        return False
        
