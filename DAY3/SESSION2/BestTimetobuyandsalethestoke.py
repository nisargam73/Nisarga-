# Best Time to buy and sale the stoke
# 1. [7,1,5,3,6,4]
# Day-2
# Buyprice=1
# Day-5
# sellatprice=6
# maxprofit=5

# 2. [7,6,4,3,1]
# profit=0

def maxProfit(prices):

    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = price - min_price
        
        if profit > max_profit:
            max_profit = profit
    return max_profit
nums=[7,1,5,3,6,4]

print(f"Max Profit Case 1: {maxProfit([7, 1, 5, 3, 6, 4])}") 
print(f"Max Profit Case 2: {maxProfit([7, 6, 4, 3, 1])}")    