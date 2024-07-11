class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                queue = []
                while stack and stack[-1]!="(":
                    queue.append(stack.pop())
                    
                stack.pop()
                while queue:
                    stack.append(queue.pop(0))
            else:
                stack.append(char)
        return ''.join(stack)
                