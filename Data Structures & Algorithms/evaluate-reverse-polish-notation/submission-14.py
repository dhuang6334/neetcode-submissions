class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = []
        for token in tokens:
            if len(token) == 1 and not token.isnumeric():
                ops.append(token)
                if (len(stack) >= 2):
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    match ops.pop():
                        case '-':
                            stack.append(operand1 - operand2)
                        case '+':
                            stack.append(operand1 + operand2)
                        case '*':
                            stack.append(operand1 * operand2)
                        case '/':
                            stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))
            print(stack)
        if len(stack) == 0:
            return 0
        return stack.pop()
        