class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer  = 0
        curMax = 0
        curMin = float("inf")
        prices.reverse()
        for i in range(len(prices)):
            curMax = max(curMax, prices[i])
            curMin = min(curMin, prices[i])

            answer = max(answer, (curMax - prices[i]))

        return answer