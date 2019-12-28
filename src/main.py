import alpaca_service as alp
import trading_strategies as ts
# soon be = GetActiveStocks
active_stocks = [
        'DHR', 
        'AMRN',
        'UBER',
        'GE',
        'PCG',
        'BAC',
        'AMD',
        'F',
        'MU',
        'NIO',
        'AAPL',
        'SNAP',
        'ECA',
        'MSFT',
        'T',
        'CMCSA',
        'BMY',
        'PFE',
        'FCX',
        'CSCO',
        'WPX',
        'M',
        'ACB',
        'ROKU',
        'VALE'
        ]


def main():
    aapl_sma = ts.sma('AAPL', 200)
    print('apple sma = ' + str(aapl_sma))

    apple_val = alp.get_value('AAPL')
    print('apple asset?')
    print(apple_val)

    account = alp.get_account()
    print('account')
    print(account)

    clock = alp.get_clock()
    print('Clock')
    print(clock)

    positions = alp.list_positions()

main()
