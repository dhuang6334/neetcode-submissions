class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26
        for char in s:
            alpha[ord(char) - ord('a')] += 1
        
        for char in t:
            alpha[ord(char) - ord('a')] -= 1
            if alpha[ord(char) - ord('a')] < 0:
                return False
        
        if sum(alpha) != 0:
            return False
        
        return True