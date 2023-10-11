#best time to buy and sell stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if prices.index(max(prices)) < prices.index(min(prices)):
        #     return max(prices) - min(prices)
        # else:
        #     for i in prices:
        for k in range(len(prices)):
            buy = min(prices)
            if prices.index(buy) == len(prices):
                return 0
            if prices.index(buy) == k:  
                  




# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
solution = Solution()
result = solution.maxProfit(prices)
print(result)