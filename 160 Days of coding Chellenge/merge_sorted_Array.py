class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        arr.sort()
        #maxi = max(arr)
        n = len(arr)
        cur_max = arr[0]
        
        if n == 1:
            return -1
            
        for i in range(n):
            if arr[i]>cur_max and arr[i] != arr[n-1]:
                cur_max = arr[i]
                
        if (cur_max != arr[n-1]):
            return cur_max
        else:
            return -1
                