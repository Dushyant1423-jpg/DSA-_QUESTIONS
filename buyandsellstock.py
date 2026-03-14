def buyandsellstock(prices):
    buyprice = float('inf')
    maxprofit = 0

    for price in prices:
        if price < buyprice:
            buyprice = price
        else:
            profit = price - buyprice
            maxprofit = max(maxprofit, profit)

    return maxprofit


prices = [7,1,5,3,6,4]
print(buyandsellstock(prices))