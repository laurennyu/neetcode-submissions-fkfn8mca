class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        # First candidate is buying on the first day, sell the next
        curr_min = prices[0]
        curr_max = prices[1]
        max_profit = max(0, curr_max - curr_min)

        for price in prices[1:]:
            if price > curr_max:
                curr_max = price
                # Consider selling at this new max price
                max_profit = max(max_profit, curr_max - curr_min)
            elif price < curr_min:
                # Consider buying at this new price
                curr_min = price
                curr_max = 0

        return max_profit