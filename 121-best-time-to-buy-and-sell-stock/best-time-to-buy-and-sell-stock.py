class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        min_so_far = prices[0]
        best = prices[1] - prices[0] 

        for x in prices[1:]:
            best = max(best, x - min_so_far)
            min_so_far = min(min_so_far, x)

        if best < 0:
            return 0

        return best

        