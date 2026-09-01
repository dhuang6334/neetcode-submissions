class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # def sig(a: str):
            
        #     adict = [0 for _ in range(26)]
            
        #     for char in a:
        #         adict[ord(char) - ord('a')] += 1

        #     return tuple(adict)

        # index = {}
        # output = []
        # for s in strs:
        #     signature = sig(s)
        #     if signature in index.keys():
        #         output[index[signature]].append(s)
        #     else:
        #         index[signature] = len(output)
        #         output.append([s])
            
        # return output

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        