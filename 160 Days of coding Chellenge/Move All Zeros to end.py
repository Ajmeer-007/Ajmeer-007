
class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	
    	left = 0
    	for right in range(len(arr)):
    	    if arr[right]!=0:
    	        arr[right],arr[left] = arr[left],arr[right]
    	        left+=1
    	return arr
