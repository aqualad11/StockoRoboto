import alpaca_service as alp
import stats

# checks the simple moving average for the long time period over the short one, then recommends whether to buy/sell
def sma_long_short(symbol, loong, short):
    # Get and format data
    long_data = alp.get_stock_data(symbol, 'day', loong)
    long_data = [l.c for l in long_data]
    short_data = [long_data[i] for i in range(short)]
    
    # Get SMA of long and short
    long_sma = stats.sma(long_data)
    short_sma = stats.sma(short_data)

    if(short_sma > long_sma):
        return true

    return false


