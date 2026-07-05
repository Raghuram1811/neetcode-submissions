class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens)==1:
            return int(tokens[0])
        
        stack = deque()
        
        for token in tokens:

            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(token))
        return stack[-1]


            
            