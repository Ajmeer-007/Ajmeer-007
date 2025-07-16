class Solution:
	def maxProduct(self,arr):
		# code here
		
		min_pro = arr[0]
		max_pro = arr[0]
		res = arr[0]
		
	    for i in range(1,len(arr)):
		    
		    temp_max = max(arr[i],min_pro*arr[i],max_pro*arr[i])
		    temp_min = min(arr[i],min_pro*arr[i],max_pro*arr[i])
		    
		    min_pro = temp_min
		    
		    max_pro = temp_max
	        res = max(res,max_pro)
	    return res
            
