class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] =1
        count = 0
        maxi = max(dic.values())
        for j,k in dic.items():
            if maxi == k:
                count+=k
        return count

