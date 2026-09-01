class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def sig(a: str):
            
            adict = [0 for _ in range(26)]
            
            for char in a:
                adict[ord(char) - ord('a')] += 1

            return tuple(adict)

        index = {}
        output = []
        for s in strs:
            signature = sig(s)
            if signature in index.keys():
                output[index[signature]].append(s)
            else:
                index[signature] = len(output)
                output.append([s])
            
        return output

        