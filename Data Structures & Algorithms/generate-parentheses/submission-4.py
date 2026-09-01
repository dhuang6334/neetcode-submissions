class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = set()



        def helper(string, i, j, a):
            if (len(string) == a):
                parenthesis.add(string)
            elif (i == j):
                string += '('
                helper(string, i+1, j, a)
            elif (a/2 > i and i > j):
                string += '('
                helper(string, i+1, j, a)
                string = string[0:-1] + ')'
                helper(string, i, j+1, a)
            else:
                string += ')'
                helper(string, i, j+1, a)

            
        helper("", 0, 0, 2*n)
        return list(parenthesis)

    