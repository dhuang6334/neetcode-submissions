class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        sig = [0] * 26

        for char in s1:
            sig[ord(char) - ord('a')] += 1

        window = [0] * 26

        l, r = 0, 0

        while (r < len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            r += 1
            if r - l >= len(s1):
                if sig == window:
                    return True

                print(window)
                window[ord(s2[l]) - ord('a')] -= 1
                
                l += 1
            
        return False
            