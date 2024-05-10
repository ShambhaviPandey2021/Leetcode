class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_map = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        sorted_score = sorted(score, reverse=True)
        rank_dict = {}
        for i, s in enumerate(sorted_score):
            rank_dict[s] = i
        ans = []
        for s in score:
            if rank_dict[s] in rank_map:
                ans.append(rank_map[rank_dict[s]])
            else:
                ans.append(str(rank_dict[s] + 1))
        return ans
