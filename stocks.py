def compute_max_profit(stock_prices):
	min_price = stock_prices[0]
	max_profit = 0

	for current in stock_prices:
		min_price = min(min_price, current)
		potential_profit = current - min_price

		if potential_profit < 0:
			min_price = current

		elif potential_profit > 0:
			if potential_profit > max_profit:
				max_profit = potential_profit

	return max_profit

stock_prices = [10, 7, 5, 8, 11, 9]
print(compute_max_profit(stock_prices))

stock_prices = [6, 15, 3, 2, 1]
print(compute_max_profit(stock_prices))