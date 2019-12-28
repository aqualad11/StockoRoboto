import alpaca_service as alp

# Simple moving average
def sma(symbol, days):
    data = alp.get_stock_data(symbol, 'day', days)

    print('data:')
    print(data)

    sumof = 0
    for d in data:
        sumof += d.c

    return sumof / days
