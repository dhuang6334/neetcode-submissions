class Solution:
    def isAnagram(strA: str, strB: str) -> bool:
        alpha = [0] * 26
        for char in strA:
            alpha[ord(char) - ord('a')] += 1
        
        for char in strB:
            alpha[ord(char) - ord('a')] -= 1
            if (alpha[ord(char) - ord('a')] < 0):
                return False
        
        if sum(alpha) != 0:
            return False
        
        return True
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def encode(strA: str) -> tuple[int]:
            alpha = [0] * 26
            for char in strA:
                alpha[ord(char) - ord('a')] += 1
            
            return tuple(alpha)
        
        check = defaultdict(list[str])
        for strA in strs:
            check[encode(strA)].append(strA)
        
        return check.values()