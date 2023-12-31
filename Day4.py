#best time to buy and sell stock

# class Solution(object):
#     def maxProfit(self, prices):
#         if not prices:
#             return 0  

#         buy = prices[0]
#         max_profit = 0

#         for price in prices:
#             if price < buy:
#                 buy = price  
#             else:
#                 max_profit = max(max_profit, price - buy)  
                

#         return max_profit

# prices = [7, 1, 5, 3, 6, 4]
# # prices = [7, 6, 4, 3, 1]
# # prices = [2, 4, 1]

# solution = Solution()
# result = solution.maxProfit(prices)
# print(result)

# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [2,4,1]


# solution = Solution()
# result = solution.maxProfit(prices)
# print(result)


#best time to buy and sell stock - part II

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0  

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit 
                        




prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
solution = Solution()
result = solution.maxProfit(prices)
print(result)