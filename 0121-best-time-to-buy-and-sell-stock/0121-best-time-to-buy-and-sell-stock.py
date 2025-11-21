class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer  = 0
        curMax = 0

        prices.reverse()
        for i in range(len(prices)):
            curMax = max(curMax, prices[i])
            answer = max(answer, (curMax - prices[i]))

        return answer