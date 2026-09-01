class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        i = 0
        out = 0
        for j, char in enumerate(s):
            count[ord(char) - ord('A')] += 1
            good = max(count[ord(s[i]) - ord('A')], count[ord(char) - ord('A')])
            total = sum(count)
            # if (total > out):
            #     out = total
            # if ((total - good) > k):
            #     if (total - 1 > out):
            #         out = total - 1 # (-1) don't count the current char 
                    
            # else:
                

            print(count)
            print(out)

            if (char != s[i]):
                if ((total - good) > k):
                    if (total - 1 > out):
                        out = total - 1
                else:
                    if (total > out):
                        out = total

                while ((total - good) > k):
                    count[ord(s[i]) - ord('A')] -= 1
                    i += 1
                    good = max(count[ord(s[i]) - ord('A')], count[ord(char) - ord('A')])
                    total = sum(count)
            else:
                if (total > out):
                    out = total
        
        return out