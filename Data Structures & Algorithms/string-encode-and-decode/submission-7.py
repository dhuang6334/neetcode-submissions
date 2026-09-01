class Solution:

    def encode(self, strs: List[str]) -> str:

        def packet(s: str):
            return str(len(s)) + "#" + s

        output = ""
        for s in strs:
            output += packet(s)

        print(output)
        return output
    def decode(self, s: str) -> List[str]:

        output = []

        count = 0
        body = False
        for c in s:
            if not body:
                if c.isnumeric():
                    count *= 10
                    count += int(c)
                elif c == "#":
                    output.append("")
                    if count > 0:
                        body = True
                    continue
                else:
                    return [] # ERROR
            else:
                count -= 1
                output[-1] += c
                if count == 0:
                    body = False

        return output