class Solution:#O(n),O(1)
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = list(s)
        ans = 0
        i=0
        while(i<len(s)):
            if i<len(s)-1:
                if s[i]=='I' and s[i+1]=='V':
                    ans+=4
                    i+=2
                    continue        
                elif s[i]=='I' and s[i+1]=='X':
                    ans+=9
                    i+=2
                    continue
                elif s[i]=='X' and s[i+1]=='L': 
                    ans+=40
                    i+=2
                    continue
                elif s[i]=='X' and s[i+1]=='C':
                    ans+=90
                    i+=2
                    continue
                elif s[i]=='C' and s[i+1]=='D':
                    ans+=400
                    i+=2
                    continue
                elif s[i]=='C' and s[i+1]=='M':
                    ans+=900
                    i+=2
                    continue
    
        
            ans+=dic[s[i]]
            i+=1

        return ans


class Solution:#O(n) with clearity
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        n = len(s)
        i=0
        while(i<n):
            if i<n-1 and dic[s[i]]<dic[s[i+1]]:
                ans+=dic[s[i+1]]-dic[s[i]]
                i+=2
            else:
                ans+=dic[s[i]]
                i+=1
        return ans 
        
