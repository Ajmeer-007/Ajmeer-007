class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        ans = arr[n-1]-arr[0]
        
        for i in range(n-1):
            maxi = max(arr[i]+k,arr[n-1]-k)
            mini = min(arr[0]+k,arr[i+1]-k)
            if mini<0:
                continue
            ans = min(ans,maxi-mini)
        return ans
