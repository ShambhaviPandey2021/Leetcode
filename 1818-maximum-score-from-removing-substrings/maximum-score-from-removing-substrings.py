class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(s, first, second, score):
            stack = []
            current_score = 0
            
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    current_score += score
                else:
                    stack.append(char)
            
            return ''.join(stack), current_score

        if x > y:
            s, score_x = remove_and_score(s, 'a', 'b', x)
            s, score_y = remove_and_score(s, 'b', 'a', y)
        else:
            s, score_y = remove_and_score(s, 'b', 'a', y)
            s, score_x = remove_and_score(s, 'a', 'b', x)
        
        return score_x + score_y

        