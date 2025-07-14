class Solution:
    def missingNumber(self, arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            if arr[i]<=0 or arr[i]>n:
                arr[i] = n+1
                
        for i in range(n):
            num = abs(arr[i])
            if 1<=num<=n:
                if arr[num-1]>0:
                    arr[num-1]*=-1
                    
        for i in range(n):
            if arr[i]>0:
                return i+1
        return n+1
