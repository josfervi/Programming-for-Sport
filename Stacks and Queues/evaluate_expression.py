# https://www.interviewbit.com/problems/evaluate-expression/

from operator import mul, div, add, sub

# O(N) time
# O(N) space

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, symbols):
        
        OPERATORS = "*/+-"
        OPERATOR_TO_FUNC = {"*": mul, "/": div, "+": add, "-": sub}
        
        stack = []
        
        for symbol in symbols:
            
            if symbol in OPERATORS:
                
                operator = symbol
                operation = OPERATOR_TO_FUNC[operator]
                
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                
                result = operation(op1, op2)
                
                stack.append(result)
                continue
            
            # symbol is a number
            number = symbol
            stack.append(number)
        
        # stack == [result]
        result = stack[0]
        return result