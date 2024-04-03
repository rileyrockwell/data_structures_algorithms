# array: ...

from typing import *

# submitted to leetcode
def maxEarnings(prices: List[int]) -> int:
      

# algomonster solution
def maxEarnings(prices: List[int]) -> int:
    max_profit = 0

    min_price = float('int')

    for price in prices:
            
            max_profit = max(max_profit, price - min_price)

            min_price = min(min_price, price)

    return max_profit


