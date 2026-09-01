class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sarr = [0 for _ in range(26)]
        tarr = [0 for _ in range(26)]

        for char in s:
            sarr[ord(char) - ord('a')] += 1
        
        for char in t:
            tarr[ord(char) - ord('a')] += 1

        for i in range(26):
            if (sarr[i] != tarr[i]):
                return False

        return True