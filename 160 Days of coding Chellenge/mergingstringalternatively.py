class Solution: #O(m+n)T ,O(1)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        left=0
        right = 0

        if len(word1) == len(word2):
            for i in range(len(word1)):
                ans+= word1[left]+word2[right]
                left+=1
                right+=1
            return ans 
        
        elif len(word1)<len(word2):
            for i in range(len(word1)):
                ans+= word1[left]+word2[right]
                left+=1
                right+=1
            ans+=word2[left:]
            return ans 
        else:
            for i in range(len(word2)):
                ans+= word1[left]+word2[right]
                left+=1
                right+=1
            ans+=word1[right:]
            return ans

#Approch2
class Solution:#O(n+m)for both
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        min_len = min(len(word1),len(word2))

        for i in range(min_len):
            ans.append(word1[i])
            ans.append(word2[i])
        ans.append(word1[min_len:])
        ans.append(word2[min_len:])

        return ''.join(ans)

        
        
