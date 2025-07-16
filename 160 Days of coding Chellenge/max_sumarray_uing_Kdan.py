class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        ans = arr[0]
        
        maxi = arr[0]
        
        for i in range(1,len(arr)):
            
            maxi = max(maxi+arr[i],arr[i])
            
            ans = max(maxi,ans)
        return ans
            
