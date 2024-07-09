class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        total = 0
        for arrival,order in customers:
            
            total += max(time- arrival,0)
       
            time = max(arrival,time)
            total += order
            time += order
        return total/len(customers)