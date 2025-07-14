from collections import Counter
class Solution:
    def findMajority(self, arr):
        # code here
        a = []
        
        dic = Counter(arr)
        n = len(arr)
        
        for (key,val) in dic.items():
            if (val>(n/3)):
                a.append(key)
        if len(a)>0:
            return sorted(a)
        return []
        
