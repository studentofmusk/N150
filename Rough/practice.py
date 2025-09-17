class Solution:
    def getRemovableIndices(self, str1: str, str2:str)->list[int]:
        
        if len(str1)-1 != len(str2):
            return [-1]
        
        res = []
        
        def dfs(i, j, skipped, index):
            if j == len(str2):
                if not skipped and i == len(str1)-1:
                    res.append(i)
                else:
                    res.append(index)
                return
            
            if not skipped:
                dfs(i+1, j, True, i)
            
            if str1[i] == str2[j]:
                dfs(i+1, j+1, skipped, index)
            
            return
        
        dfs(0, 0, False, None)
            
        return res
    
print(Solution().getRemovableIndices("aaabb", "aaab"))