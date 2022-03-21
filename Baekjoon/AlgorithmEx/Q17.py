# 17-1
# 최대 수익 알고리즘
def max_profit(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit

stock = [10300, 7200, 8300, 9000, 6400, 10500, 7340, 2300]
print(max_profit(stock))

# 17-2
# 최대 수익 알고리즘2
def max_profit2(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]
    for i in range(1,n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit

stock = [9800, 7300, 3800, 9000, 4600, 10100, 7200, 4500]
print(max_profit2(stock))
