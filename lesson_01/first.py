raw_price1 = "1,234.50"
raw_price2 = " 98.75 "
raw_return1 = "2.63%"
raw_return2 = "-1.45%"
raw_ticker = " msft "
missing = "N/A"

# pulizia

ticker = raw_ticker.strip().upper()
price = float(raw_price1.replace(",", ""))
price2 = float(raw_price2.strip())
returns1 = float(raw_return1.replace("%", "")) / 100
returns2 = float(raw_return2.replace("%", "")) / 100

if missing == "N/A":
    miss = None
else:
    miss = float(miss)


print(f"Ticker: {ticker}")
print(f"prezzo: {price}")
print(f"prezzo: {price2}")
print(f"return: {returns1:.2%}")
print(f"return: {returns2:.2%}")
print(f"missing: {miss}")
