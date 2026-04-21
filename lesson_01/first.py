import math

prices = [100.0, 102.0, 101.5, 104.0, 103.2]

simple_return_day2 = (prices[1] - prices[0]) / prices[0]
simple_return_day3 = (prices[2] - prices[1]) / prices[1]
simple_return_day4 = (prices[3] - prices[2]) / prices[2]
simple_return_day5 = (prices[4] - prices[3]) / prices[3]

log_return_day2 = math.log(prices[1] / prices[0])
log_return_day3 = math.log(prices[2] / prices[1])
log_return_day4 = math.log(prices[3] / prices[2])
log_return_day5 = math.log(prices[4] / prices[3])


print(
    "Day 2 | Simple:", round(simple_return_day2, 4), "| Log:", round(log_return_day2, 4)
)
print(
    "Day 3 | Simple:", round(simple_return_day3, 4), "| Log:", round(log_return_day3, 4)
)
print(
    "Day 4 | Simple:", round(simple_return_day4, 4), "| Log:", round(log_return_day4, 4)
)
print(
    "Day 5 | Simple:", round(simple_return_day5, 4), "| Log:", round(log_return_day5, 4)
)
