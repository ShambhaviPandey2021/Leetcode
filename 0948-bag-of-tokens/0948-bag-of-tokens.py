class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r = 0,len(tokens)-1
        score = 0
        max_score = 0
        while l<=r:
            if power>=tokens[l]:
                power -= tokens[l]
                score +=1
                l +=1
            elif score>0:
                power+=tokens[r]
                score-=1
                r-=1
            else:
                break;
            max_score = max(max_score,score)
        return max_score
                
        
        