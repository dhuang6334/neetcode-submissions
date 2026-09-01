class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            size = len(word)
            out += str(size)
            out += '\u03A9' # can be any delimiter 
            out += word

        return out
    def decode(self, s: str) -> List[str]:
        out = []
        num = ""
        length = len(s)
        i = 0
        while i < length:
            if (s[i].isascii()): # anything thats not that delimiter (must be part of the number)
                num += s[i]
                i += 1
            else:
                count = int(num)
                word = ""
                i += 1
                for j in range(count):
                    word += s[i+j]
                i += count
                out.append(word)
                num= ""

        return out