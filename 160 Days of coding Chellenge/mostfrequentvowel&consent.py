class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic = {}
        vowel = ['a','e','i','o','u']
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] =1
            
        v_max = 0
        c_max = 0

        for i,j in dic.items():
            if i in vowel:
                if j>v_max:
                    v_max= j
            else:
                if j>c_max:
                    c_max = j

        return (v_max+c_max)
        

