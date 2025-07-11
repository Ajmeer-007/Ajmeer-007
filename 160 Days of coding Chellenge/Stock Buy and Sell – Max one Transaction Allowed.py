class Solution:
    def maximumProfit(self, prices):
        # code here
        mini = prices[0]
        ans = 0
        
        for i in  range(len(prices)):
            mini = min(mini,prices[i])
            
            ans = max(ans,prices[i]-mini)
        return ans
