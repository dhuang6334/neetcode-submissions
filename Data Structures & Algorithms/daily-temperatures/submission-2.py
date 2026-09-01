class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = []
        for i in range(len(temperatures) - 1, -1, -1):
            if (i == len(temperatures) - 1):
                stack.append((temperatures[i],i))
                out.append(0)
            elif (temperatures[i] >= temperatures[i+1]):
                high = i
                while(len(stack) > 0 and stack[-1][0] <= temperatures[i]):
                    stack.pop()
                if (len(stack) > 0):
                    high = stack[-1][1]
                stack.append((temperatures[i], i))
                out.append(high - i)
            else:
                stack.append((temperatures[i],i))
                out.append(1)
        out = list(out)
        out.reverse()
        print(out)
        return out