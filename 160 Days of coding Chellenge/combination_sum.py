class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def check(start,path,total):
            if total == target:
                result.append(path[:])
                return 
            if total>target:
                return 
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                check(i,path,candidates[i]+total)
                path.pop()


        check(0,[],0)
        return result
