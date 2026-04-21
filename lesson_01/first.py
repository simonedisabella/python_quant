ticker = "AAPL"
price_yesterday = "182.5"
price_today = "187.3"

simple_return = (float(price_today) - float(price_yesterday)) / float(price_yesterday)

print(ticker + ":", round(simple_return, 4))
