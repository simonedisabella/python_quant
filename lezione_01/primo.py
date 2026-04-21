ticker = "AAPL"
prezzo_ieri = "182.5"
prezzo_oggi = "187.3"

simple_return = (float(prezzo_oggi) - float(prezzo_ieri)) / float(prezzo_ieri)

print(ticker + ":", round(simple_return, 4))
