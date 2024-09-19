class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele == '+' or ele == '-' or ele == '/' or ele == '*':
                ope2, ope1 = stack.pop(), stack.pop()
                match ele:
                    case '+':
                        stack.append(ope1 + ope2)
                    case '-':
                        stack.append(ope1 - ope2)
                    case '/':
                        truncated = math.trunc(ope1 / ope2)
                        stack.append(truncated)
                    case '*':
                        stack.append(ope1 * ope2)
                    case _:
                        print("invalid operator")
            else:
                stack.append(int(ele))
        
        return stack.pop()