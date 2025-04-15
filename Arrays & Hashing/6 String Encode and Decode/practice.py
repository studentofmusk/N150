from typing import List    
class Solution:

    def encode(self, strs: List[str]) -> str:
        enstr = ""
        for s in strs:
            enstr += f"{len(s)}#{s}"
        
        return enstr
    
    def decode(self, s: str) -> List[str]:
        DList= []
        i = 0
        if len(s) < 3:
            return []
        
        while i < len(s):
                
            if s[i].isnumeric() and s[i+1] == "#":
                DList.append(s[i+2:i+2+int(s[i])])
                i += 2+int(s[i])
            
        return DList

solution = Solution()
Hash = solution.encode(["neet","code","love","you"])
print(Hash)
print(solution.decode(Hash))