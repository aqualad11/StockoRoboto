import alpaca_service as alp

# Simple moving average
def sma(data):
    sumof = 0
    for d in data:
        sumof += d

    return sumof / len(data)


