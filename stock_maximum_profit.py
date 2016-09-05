'''
The cost of a stock on each day is given in an array,
find the max profit that you can make by buying and
selling in those days. For example, if the given array is
{100, 180, 260, 310, 40, 535, 695}, the maximum profit can
earned by buying on day 0, selling on day 3. Again buy on 
day 4 and sell on day 6. If the given array of prices is 
sorted in decreasing order, then profit cannot be earned at all.
'''

# f we are allowed to buy and sell only once, then we can use following algorithm.
prices = [100, 180, 260, 310, 40, 535, 695] 

minimum_price = None
max_profit_pair = None
max_profit = None

for i,val in enumerate(prices):
    if minimum_price is None or prices[i] < prices[minimum_price]:
        minimum_price = i
    print minimum_price,i
    if prices[i] - prices[minimum_price] > max_profit:
        max_profit_pair = (minimum_price,i)
        max_profit = prices[i] - prices[minimum_price]
    print max_profit


print 'The most ideal (buy,sell) pair would be:',max_profit_pair
print 'In other words, buy on day',max_profit_pair[0],'and sell on day',max_profit_pair[1]
