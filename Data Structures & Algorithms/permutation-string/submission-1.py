class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        sig = {}

        for char in s1:
            sig[char] = sig.get(char, 0) + 1

        window = {}

        l, r = 0, 0

        while (r < len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            r += 1
            if r - l >= len(s1):
                if sig == window:
                    return True

                print(window)
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1
            
        return False
            