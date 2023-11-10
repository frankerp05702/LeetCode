from math import floor
from typing import List

class Solution:
    def partialProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        partial=[]
        # Create subarrays max min and calculate max profit
        for i in range(len(prices)):
            if i==0:
                # start appending
                partial.append(prices[i])
            else:
                # Find edge to reset appending
                if prices[i]<prices[i-1]:
                    # Order partial calculation
                    max_profit+=self.partialProfit(partial)
                    # Reset partial
                    partial=[]
                    # Append i
                    partial.append(prices[i])
                else:
                    # keep appending
                    partial.append(prices[i])

        max_profit+=self.partialProfit(partial)
        return max_profit





# Example 1
prices = [7,1,5,3,6,4]

s = Solution()
print(s.maxProfit(prices))


# Example 2
prices = [1,2,3,4,5]

s = Solution()
print(s.maxProfit(prices))

# Example 3
prices = [7,6,4,3,1]

s = Solution()
print(s.maxProfit(prices))