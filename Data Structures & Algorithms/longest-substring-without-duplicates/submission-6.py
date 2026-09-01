class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0

        count = 0

        window = set()

        while r < len(s):
            if s[r] in window:
                window.remove(s[l])
                l += 1
            else:
                window.add(s[r])
                r += 1
                count = max(len(window), count)
            
        return count
