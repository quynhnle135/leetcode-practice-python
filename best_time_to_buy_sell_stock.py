def maxProfit(prices):
    current_profit = 0
    max = -10000
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max:
                max = prices[j] - prices[i]
                current_profit = max
    return current_profit

print(max([7,1,5,3,6,4]))