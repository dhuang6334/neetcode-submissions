class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        out = 0
        curr = 0
        i = 0
        for j, char in enumerate(s):
            if char in check:
                dup = True
                sub = set()
                
                while (dup):
                    i += 1
                    sub = set(s[i:j+1])
                    #print(sub)
                    
                    size = j - i + 1
                    if len(sub) == size:
                        dup = False
                
                check = sub
                curr = len(check)
            else:
                check.add(char)
                print(check)
                curr += 1

                if (curr > out):
                    out = curr
        
        # check = set()
        # curr = 0
        # for char in s[::-1]:
        #     if char in check:
        #         check = set()
        #         check.add(char)
        #         curr = 1
        #     else:
        #         check.add(char)
        #         curr += 1

        #         if (curr > out):
        #             out = curr
        
        return out
