class Solution:
    def circularSubarraySum(self, arr):
    # code here
        summ = sum(arr)
        maxi_val = self.maxi(arr)
        mini_val = self.mini(arr)
    
        if maxi_val<0:
            return maxi_val
    
        return max(maxi_val,summ-mini_val)
    
    def maxi(self,arr):
        maxi_curr = maxi_so_for = arr[0]
        for i in (arr[1:]):
            maxi_curr = max(i,maxi_curr+i)
            maxi_so_for = max(maxi_so_for,maxi_curr)
        return maxi_so_for
        
    def mini(self,arr):
        mini_curr = mini_so_for = arr[0]
        for j in arr[1:]:
            mini_curr = min(j,mini_curr+j)
            mini_so_for = min(mini_so_for,mini_curr)
        return mini_so_for
