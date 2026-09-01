class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = set()
        # for i in range(n):
        #     if (len(parenthesis) == 0):
        #         parenthesis.add("()")
        #     else:
        #         new = set()
        #         for para in parenthesis:
        #             new.add('('+para+')')
        #             new.add("()"+para)
        #             new.add(para+"()")
        #         parenthesis = new



        def helper(string, i, j, a):
            if (len(string) == a):
                print("hi")
                parenthesis.add(string)
                print(string)
            elif (i == j):
                print("yo")
                string += '('
                print(string)
                helper(string, i+1, j, a)
            elif (a/2 > i and i > j):
                string += '('
                print(string)
                helper(string, i+1, j, a)
                string = string[0:-1] + ')'
                print(string)
                helper(string, i, j+1, a)
            else:
                print("yo")
                string += ')'
                print(string)
                helper(string, i, j+1, a)

            
        helper("", 0, 0, 2*n)
        return list(parenthesis)

    