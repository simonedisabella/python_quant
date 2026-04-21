ticker1 = "AAPL"
price_yesterday1 = "182.5"
price_today1 = "187.3"

ticker2 = "MSFT"
price_yesterday2 = "331.2"
price_today2 = "329.8"

ticker3 = "TSLA"
price_yesterday3 = "245.0"
price_today3 = "251.6"


return1 = (float(price_today1) - float(price_yesterday1)) / float(price_yesterday1)
return2 = (float(price_today2) - float(price_yesterday2)) / float(price_yesterday2)
return3 = (float(price_today3) - float(price_yesterday3)) / float(price_yesterday3)


print(f"AAPL: {return1:.2%}")
print(f"MSFT: {return2:.2%}")
print(f"TSLA: {return3:.2%}")
